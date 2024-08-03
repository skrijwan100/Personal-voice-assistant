# from openai import OpenAI

# client = OpenAI(
#  api_key="sk-proj-NsNx2WZ7NECJTh8VVJanT3BlbkFJuLFXJLEHK66DUKE0GJBr",
# )
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a parsonal ssistant,your name is jarvis, skilled in explaining complex programming concepts with creative flair like google."},
#     {"role": "user", "content": "what is coding"}
#   ]
# )

# print(completion.choices[0].message)

from openai import OpenAI,error
import time

def get_chat_completion(api_key, model, messages, retries=3, backoff_factor=1):
    client = OpenAI(api_key=api_key)
    
    for attempt in range(retries):
        try:
            completion = client.chat.completions.create(
                model=model,
                messages=messages
            )
            return completion
        except error.RateLimitError as e:
            if attempt < retries - 1:
                time.sleep(backoff_factor * (2 ** attempt))
            else:
                raise e

api_key = ""
model = "gpt-3.5-turbo"
messages = [
    {"role": "system", "content": "You are a personal assistant, your name is Jarvis, skilled in explaining complex programming concepts with creative flair like Google."},
    {"role": "user", "content": "what is coding"}
]

completion = get_chat_completion(api_key, model, messages)
print(completion)