import os
import cohere as co
import re

# Set up your API key
api_key = os.environ.get("CO_API_KEY")


# Create a client instance


# # Define your prompt
# prompt = "Send me a tenor link to gif that is related to a meme in July 16, 2006"
# # Generate text using the prompt
# response = client.chat()

# # Print the generated text
# print(response)



# print(response)

# print("******************************")

# print(response.text)

# pattern = r"\[([\s\S]*?)\]"

# # Use re.search to find the pattern in the input string
# match = re.search(pattern, response.text)

# # Check if a match is found
# if match:
#     # Extract the groups from the match object and create a list
#     extracted_list = list(match.groups())
#     print(extracted_list)
# else:
#     print("No match found.")


class LLM:
    def __init__(self, data, api=api_key, model="command"):
        # Add your initialization code here
        self.api = api
        self.client = co.Client(api)
        self.model = model
        self.data = data


    def get_movies_by_year(self):
        year = self.data.get("year")
        # Add your method code here
        if year > 2021 or year < 1995:
            return "invalid year"
        
        prompt = f"Give 10 movie names from {year} and format movie names by comma seperation (DO NOT PUT ANY OTHER TEXT)"

        response = self.client.chat(
            message=prompt, 
            model=self.model,
            connectors=[{"id": "web-search",
                        }],
            temperature=1.0,   
        )
        
        # print()
        # print()
        # print(response.text)
        # print()
        # print()
        # print("abcdef")

        return response.text
    
    def parse_response(self):
        text = self.get_movies_by_year()
        text = text.strip()
        text = text.replace("\n", "")
        # print(text)
        # pattern = r"\[([\s\S]*?)\]"
        # extracted_list = []
        # # Use re.search to find the pattern in the input string
        # match = re.search(pattern, text)
        
        # # Check if a match is found
        # if match:
        #     # Extract the groups from the match object and create a list
        #     extracted_list = list(match.groups())

        #     for index, s in enumerate(extracted_list):
        #         extracted_list[index] = extracted_list[index].replace("\n", "")

        #         extracted_list[index] = extracted_list[index].replace("\\", "")
            
        #     print(extracted_list)
        # else:
        #     print("No match found.")


        pattern = r':(.+)'
        # pattern = r"(?<=: ).*"

        # Use regex to find the movie names after the colon
        match = re.search(pattern, text)

        parsed_list = []

        if match:
            # Extract the matched group and create a list
            parsed_list = [movie.strip() for movie in match.group(1).split(',')]

            # Print the resulting list
            print(parsed_list)
        else:
            print("No matches found.")
        
        return parsed_list
        
    
# def main():
#     # LLM INSTANCE
#     llm = LLM({"year": 2002})
#     llm.parse_response()
# #     myString = """Here is a list of 10 movies released in 1998 in CSV format:

# # There's Something About Mary, Saving Private Ryan, Shakespeare in Love, Armageddon, The Big Lebowski, Rush Hour, The Truman Show, Primary Colors, American History X, Rushmore"""
# #     myString = myString.strip()
# #     myString = myString.replace("\n", "")
# #     print(myString)

# if __name__ == "__main__":
#     main()