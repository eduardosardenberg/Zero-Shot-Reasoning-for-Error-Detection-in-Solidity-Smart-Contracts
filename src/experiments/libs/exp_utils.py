import pandas as pd
from libs.openai import call_openai
import libs.prompts as prompts
from tqdm import tqdm
from sklearn.metrics import precision_score, recall_score, f1_score, confusion_matrix
import json

def classify_dataset(df, prompt_function, model_name):

    results = []
    for _, row in tqdm(df.iterrows()):
        file_path = row['file_path']
        file_name = row['file_name']

        prompt_txt = prompt_function("../../Datasets/{}".format(file_path))
        response = call_openai(model_name,prompt_txt)
        response = extract_json_from_text(response)

        if response:
            try:
                result = json.loads(response)
                results.append({
                    "predicted_has_error": result["has_error"],
                    "actual_has_error": row["has_error"],
                    "bug_type": result["bug_type"]
                #"location": result["location"]
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
        # Find the start and end of the JSON in the text
        start = text.find("{")
        end = text.rfind("}") + 1

        # Extract and convert the JSON into a dictionary
        json_str = text[start:end]
        return json_str
    
    except Exception as e:
        print(f"Error extracting JSON: {e}")
        print(f"Full text: {text}")
        return None
