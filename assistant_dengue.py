import sys
import re
from gpt4all import GPT4All
import google.generativeai as genai

if len(sys.argv) > 1:
    input_text = ' '.join(sys.argv[1:])

gemini_key = ""

genai.configure(api_key = gemini_key)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
        
model = genai.GenerativeModel('gemini-pro')

response = model.generate_content(input_text)

print(response.text)