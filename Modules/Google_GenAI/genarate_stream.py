from dotenv import load_dotenv
import os
from google import genai
import pathlib

# Load environment variables from .env file
env_path = pathlib.Path(__file__).parent / ".env"
load_dotenv(env_path)

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# Use the powerful 2.5 Pro model
model_id = "gemini-2.5-flash-lite-latest"

response = client.models.generate_content_stream(
    model=model_id,
    contents=input(f"Ask {model_id}: "),
)

for stream in response:
    print(stream.text, end="")