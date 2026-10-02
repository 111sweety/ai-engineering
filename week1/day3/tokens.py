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
prompt1="Hi!"
prompt2="Explain time travel in detail"
prompt3="Write a 1000 word essay on the impact of climate change on global ecosystems."
prompt="Write a short poem about the beauty of nature."

prompts=[prompt1, prompt2, prompt3, prompt]

for prompt in prompts:
    message={
    "role": role,
    "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages, max_tokens=500)
    usage=response.usage
    print(f"Prompt:{prompt} -->your total tokens used :{usage.total_tokens} , prompt tokens:{usage.prompt_tokens} , completion tokens:{usage.completion_tokens} finish reason:{response.choices[0].finish_reason}")
    
 



# response=client.chat.completions.create(model=model,messages=messages)
# print(response.choices[0].message.content)