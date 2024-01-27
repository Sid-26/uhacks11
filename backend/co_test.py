import os
import cohere

# Set up your API key and model ID
api_key = os.environ.get("COHERE_API_KEY")
model_id = "command"

# Create a client instance
client = cohere.Client(api_key)

# # Define your prompt
# prompt = "Send me a tenor link to gif that is related to a meme in July 16, 2006"
# # Generate text using the prompt
# response = client.chat()

# # Print the generated text
# print(response)


