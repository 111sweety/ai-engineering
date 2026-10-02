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


from pydantic import BaseModel
class Ticket(BaseModel):
    name: str
    device: str
    issue: str
    address: str
    email: str
    contact_number: str
    
schema=Ticket.schema_json()
response_format={
    "type": "json_object",
}

system_prompt=f"""
    extract the personal information from the ticket strictly based on this schema and give a json output {schema}"""
    
messsage_system={
    
    "role": "system",
    "content": system_prompt
}

text="hello my name is sweety. i have an iphone which is not working at all. my address is delhi.my email is abc@gmail.com.my contact number is 9876543"
prompt=f""" 
    this is a customer ticket. please extract the personal information from this . {text}
"""
message={
    "role": role,
    "content":prompt
}

messages=[messsage_system, message]

response=client.chat.completions.create(model=model,messages=messages, response_format=response_format)
print(response.choices[0].message.content)



import json
raw_json = response.choices[0].message.content
data_file = json.loads(raw_json)
ticket=Ticket(**data_file)

print(ticket.name)
print(ticket.device)
print(ticket.issue)
print(ticket.address)