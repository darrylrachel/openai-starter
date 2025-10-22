from dotenv import load_dotenv
from openai import OpenAI
from typing import List, Dict, Optional
import requests
import json

load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = """

"""

response = client.chat.completions.create(
    model="",
    response_format= {},
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": "Welcome, my friend ♥" }
    ]
)
