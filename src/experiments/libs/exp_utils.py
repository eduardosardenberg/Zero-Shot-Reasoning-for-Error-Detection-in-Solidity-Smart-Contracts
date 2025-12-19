import pandas as pd
from openai_lib import call_openai
from gemini_lib import call_gemini
from anthropic_lib import call_anthropic
import prompts as prompts
from tqdm import tqdm
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
import json
import re


def classify_dataset_stop_on_fn(df, prompt_function, model_name):
    results = []
    for _, row in tqdm(df.iterrows()):
        file_path = row['file_path']
        file_name = row['file_name']

        prompt_txt = prompt_function("../../../Datasets/{}".format(file_path))
        response = call_openai(model_name, prompt_txt)
        response = extract_json_from_text(response)

        if response:
            try:
                result = json.loads(response)
                predicted = result["has_error"]
                actual = row["has_error"]

                results.append({
                    "predicted_has_error": predicted,
                    "actual_has_error": actual,
                    "bug_type": result["bug_type"],
                    "location": result["location"]
                })

                # Checagem do falso negativo
                if (predicted == True) and (actual == False):
                    print("Falso positivo encontrado:")
                    print({
                        "predicted_has_error": predicted,
                        "actual_has_error": actual,
                        "bug_type": result["bug_type"],
                        "location": result["location"],
                        "file_name": file_name
                    })
                    # Retorna resultados até o momento ou só o falso negativo, conforme sua preferência:
                    return pd.DataFrame(results)

            except json.JSONDecodeError as e:
                print(response)
                print(f"Error decoding JSON for {file_name}: {e}")

    # Se não encontrar nenhum falso negativo, retorna todos
    return pd.DataFrame(results)



def classify_dataset(df, prompt_function, model_name):
    results = []
    for _, row in tqdm(df.iterrows()):
        file_path = row['file_path']
        file_name = row['file_name']

        prompt_txt = prompt_function("../../../Datasets/{}".format(file_path))
        response = call_openai(model_name,prompt_txt)
        response = extract_json_from_text(response)

        if response:
            try:
                result = json.loads(response)
                results.append({
                    "predicted_has_error": result["has_error"],
                    "actual_has_error": row["has_error"],
                    "bug_type": result["bug_type"],
                    "location": result["location"]
                })
            except json.JSONDecodeError as e:
                print(response)
                print(f"Error decoding JSON for {file_name}: {e}")

    # Convert the results into a DataFrame
    results_df = pd.DataFrame(results)
    return results_df

def classify_dataset_gemini(df, prompt_function, model_name):
    results = []
    for _, row in tqdm(df.iterrows()):
        file_path = row['file_path']
        file_name = row['file_name']

        prompt_txt = prompt_function("../../../Datasets/{}".format(file_path))
        response = call_gemini(model_name,prompt_txt)
        response = extract_json_from_text(response)

        if response:
            try:
                result = json.loads(response)
                results.append({
                    "predicted_has_error": result["has_error"],
                    "actual_has_error": row["has_error"],
                    "bug_type": result["bug_type"],
                    "location": result["location"]
                })
            except json.JSONDecodeError as e:
                print(response)
                print(f"Error decoding JSON for {file_name}: {e}")

    # Convert the results into a DataFrame
    results_df = pd.DataFrame(results)
    return results_df

def classify_dataset_anthropic(df, prompt_function, model_name):
    results = []
    for _, row in tqdm(df.iterrows()):
        file_path = row['file_path']
        file_name = row['file_name']

        prompt_txt = prompt_function("../../../Datasets/{}".format(file_path))
        response = call_anthropic(model_name,prompt_txt)
        response = extract_json_from_text(response)
        
        if response:
            try:
                result = json.loads(response)
                results.append({
                    "predicted_has_error": result["has_error"],
                    "actual_has_error": row["has_error"],
                    "bug_type": result["bug_type"],
                    "location": result["location"]
                })
            except json.JSONDecodeError as e:
                print(response)
                print(f"Error decoding JSON for {file_name}: {e}")

    # Convert the results into a DataFrame
    results_df = pd.DataFrame(results)
    return results_df

def evaluate_experiment(results_df):

    results_df['actual_has_error'] = results_df['actual_has_error'].astype(int)
    results_df['predicted_has_error'] = results_df['predicted_has_error'].astype(int)

    # Calculate recall, precision, and f1-score
    precision = precision_score(results_df['actual_has_error'], results_df['predicted_has_error'], zero_division=0)
    recall = recall_score(results_df['actual_has_error'], results_df['predicted_has_error'], zero_division=0)
    f1 = f1_score(results_df['actual_has_error'], results_df['predicted_has_error'], zero_division=0)
    
    # Calculate the confusion matrix
    conf_matrix = confusion_matrix(results_df['actual_has_error'], results_df['predicted_has_error'])
    
    return precision*100, recall*100, f1*100, conf_matrix

def extract_json_from_text(text):
    if not text:
        print("extract_json_from_text: recebeu texto vazio ou None!")
        print("Texto com erro:", text)
        return None
    try:
        # Procura só o primeiro bloco JSON (do primeiro { até o primeiro } depois dele)
        match = re.search(r'({.*?})', text, re.DOTALL)
        if match:
            json_str = match.group(1)
            return json_str  # Continua retornando string JSON
        else:
            print("Nenhum bloco JSON encontrado no texto!")
            print("Texto com erro:", text)
            return None
    except Exception as e:
        print(f"Error extracting JSON: {e}")
        print(f"Full text: {text}")
        return None

