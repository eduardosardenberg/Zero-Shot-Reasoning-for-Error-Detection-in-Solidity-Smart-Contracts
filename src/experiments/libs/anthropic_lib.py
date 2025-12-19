import os
import time
from anthropic import Anthropic
from dotenv import load_dotenv
import tiktoken

load_dotenv()
client = Anthropic()

def call_anthropic(model_name, prompt, max_attempts=2, timeout=20, max_tokens=4096, max_input_tokens=10000):
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(prompt)
    if len(tokens) > max_input_tokens:
        #print(f"Prompt será truncado: {len(tokens)} tokens > limite de {max_input_tokens}")
        tokens = tokens[:max_input_tokens]
        prompt = enc.decode(tokens)
    
    attempt = 0
    rate_limited = False
    while attempt < max_attempts:
        try:
            response = client.messages.create(
                model=model_name,
                max_tokens=max_tokens,
                temperature=0.0,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.content[0].text.strip()
        except Exception as e:
            error_str = str(e)
            print(f"Attempt {attempt+1} failed: {e}")
            if "429" in error_str or "rate_limit_error" in error_str:
                if rate_limited:
                    print("Rate limit atingido novamente. Não vou tentar mais.")
                    break
                print("Rate limit atingido. Tentando mais uma vez após esperar 30 segundos...")
                time.sleep(30)
                rate_limited = True
            else:
                time.sleep(1)
            attempt += 1
    return {}
