from openai import OpenAI
from dotenv import load_dotenv
import os
from datetime import datetime

# Load API key
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarize_text(text):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an assistant that converts conversations into structured meeting summaries. Extract key points, decisions, and important details clearly."
            },
            {
                "role": "user",
                "content": text
            }
        ]
    )
    print(response)
    summary = response.choices[0].message.content

    # Add timestamp
    now = datetime.now()
    date = now.strftime("%Y-%m-%d")
    time = now.strftime("%H:%M:%S")

    return {
        "date": date,
        "time": time,
        "summary": summary
    }