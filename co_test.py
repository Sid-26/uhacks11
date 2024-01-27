import cohere

# Set up your API key and model ID
api_key = "5kyHPS2LlP2YzeAhE57nkZJDIoY1JM1LnU0jXnWt"
model_id = "command"

# Create a client instance
client = cohere.Client(api_key)

# Define your prompt
prompt = "List top 10 songs from billboard year end hot singles chart in 2016, don't give descriptions only song names and make sure they are in order and take it from wikipedia."

# Generate text using the prompt
response = client.generate(prompt, model=model_id)

# Print the generated text
print(response)


