import requests

def lambda_handler(event, context):
    url = "https://api.quotable.io/random"
    response = requests.get(url)

    if response.status_code == 200:
        quote_data = response.json()
        content = quote_data.get("content")
        author = quote_data.get("author")
        print(f"Random Quote: '{content}' - {author}")
        print("v1.2")
    else:
        print(f"Failed to retrieve a random quote. Status code: {response.status_code}")

