import os
import time
import google.generativeai as genai
from dotenv import load_dotenv
import tiktoken

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def call_gemini(model_name,prompt,max_attempts=3,max_input_tokens=17000):
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(prompt)
    if len(tokens) > max_input_tokens:
        print(f"Prompt será truncado: {len(tokens)} tokens > limite de {max_input_tokens}")
        tokens = tokens[:max_input_tokens]
        prompt = enc.decode(tokens)
    
    attempt = 0
    model = genai.GenerativeModel(model_name)
    while attempt < max_attempts:
        try:
            response = model.generate_content(
                prompt,
                generation_config={
                    "temperature": 0.0,
                    "candidate_count": 1
                }
            )
            return response.text.strip()
        except Exception as e:
            error_str = str(e)
            print(f"Attempt {attempt+1} failed: {e}")
            if "504" in error_str or "timeout" in error_str:
                print("Timeout recebido. Tentando novamente após esperar 15 segundos...")
                time.sleep(15)
            else:
                time.sleep(2)
            attempt += 1
    return {}
