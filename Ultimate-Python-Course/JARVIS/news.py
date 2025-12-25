import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

newsapi = os.getenv("NEWS_API_KEY")

def get_news():
    # 1. Define the URL (Top headlines in India/US)
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"
    # 2. Use requests.get to fetch the data
    response = requests.get(url)
    # 3. Check if the request was successful
    if response.status_code == 200:
        # Convert the response into a Python dictionary
        data = response.json()
        
        # 4. Extract the articles
        articles = data.get('articles', [])
        
        headlines = []
        for article in articles[:5]:
            headlines.append(article['title'])
        return headlines
    else:
        print(f"Error fetching news: {response.status_code}")
        return []
if __name__ == "__main__":
    print(get_news())