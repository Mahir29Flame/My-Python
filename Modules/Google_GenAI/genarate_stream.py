from google import genai
from google.genai import types
import os


client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

response = client.models.generate_content_stream(
    model="gemini-flash-lite-latest",
    content = input(f"Ask {model}: "),
)

for stream in response:
    print(stream.text)