import requests

url = input("Paste Cloudflare URL (without /chat): ").strip()
api_url = url + "/chat"

print("Connected! Type 'exit' to quit.\n")

while True:
    msg = input("You: ")

    if msg.lower() == "exit":
        break

    response = requests.post(api_url, json={"message": msg})
    print("Bot:", response.json()["response"])