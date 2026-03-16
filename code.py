import requests
import sys
import json

topic = input("Enter topic: ")

url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"

headers = {
    'User-Agent': 'MyPythonScript/1.0 (your-email@example.com)'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:

    data = response.json()
    print(json.dumps(data, indent=4))

    title = data["title"]
    summary = data["extract"]

    print(f"\nTitle: {title}")
    print(f"\nSummary: {summary}")

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(f"Topic: {title}\n\n")
        f.write(summary)

    print("\nSummary saved to output.txt")

else:
    print(f"Error: Unable to fetch data for topic '{topic}'. Status code: {response.status_code}")