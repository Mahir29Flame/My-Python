import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Initialize the client using the key from environment variables
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Using the new GPT-5 Responses API
response = client.responses.create(
    model="gpt-5-nano",
    input="Write a one-sentence bedtime story about a unicorn.",
)

# In the new API, the output is in response.output_text
print(response.output_text)