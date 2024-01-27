import os
import cohere as co

# Set up your API key and model ID
api_key = os.environ.get("CO_API_KEY")
model_id = "command"

# Create a client instance
client = co.Client(api_key)

# # Define your prompt
# prompt = "Send me a tenor link to gif that is related to a meme in July 16, 2006"
# # Generate text using the prompt
# response = client.chat()

# # Print the generated text
# print(response)

response = client.chat(
    message="Send me a link of an image of nyan cat", 
    model=model_id,
    connectors=[{"id": "web-search",
                 }],
    temperature=0.75,
    
    )

print(response)

print("******************************")

print(response.text)