import os
from openai import OpenAI
from dotenv import load_dotenv
import time

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# Use the OpenAI API to execute the prompt
def call_openai(model_name, prompt, max_attempts=1, timeout=20):
    attempt = 0
    while attempt < max_attempts:
        try:
            completion = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                response_format = { "type": "json_object" },
                #temperature = 0.0,
                seed = 64,
                timeout = timeout,
            )
            return completion.choices[0].message.content.strip()
        except Exception as e:
            print(f"Attempt {attempt+1} failed: {e}")
            attempt += 1
            if attempt < max_attempts:
                time.sleep(1)
    return {}
