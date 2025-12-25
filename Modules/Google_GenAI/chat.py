import os
from google import genai
from dotenv import load_dotenv
import pathlib

# Load environment variables from .env file
env_path = pathlib.Path(__file__).parent / ".env"
load_dotenv(env_path)

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# Use the standard 2.5 Flash model
model_id = "gemini-2.5-flash" 

chat = client.chats.create(model=model_id)

print(f"Chat with {model_id} (Type '/exit' to quit)")

while True:
    try:
        user_input = input("You: ")
        if user_input.lower() == "/exit":
            break
        
        response = chat.send_message(user_input)
        print(f"Gemini: {response.text}")
    except KeyboardInterrupt:
        print("\nExiting...")
        break
    except Exception as e:
        print(f"Error: {e}")