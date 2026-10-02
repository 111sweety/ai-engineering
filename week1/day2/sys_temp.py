import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client=Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"
role="user"
# prompt="i love you baby !"
prompt="Suggest a name for my food company and name should be in one word."


message_system={
    "role": "system",
    # "content": "you are my loving girlfriend"
    # "content": "you are my strict office colleague who is also my manager"
    "content": "you are a brand managerwho suggests name for my food company and name should be in one word.suggest one name only"
    
    
}
message={
    "role": role,
    "content":prompt
}

messages=[message_system, message]
# by default temperature is 0 means safe , range is [0,2] , higher the temperature more creative the response
response=client.chat.completions.create(model=model,messages=messages, temperature=2)
print(response.choices[0].message.content)