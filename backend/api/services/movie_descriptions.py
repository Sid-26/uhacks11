import cohere as co
import os

api_key = os.environ.get("CO_API_KEY")

class Chat:
    def __init__(self, data, api=api_key, model="command"):
        self.api = api
        self.client = co.Client(api)
        self.model = model
        self.data = data
    
    def ask_cohere_movie_fact(self):
        movie = self.data.get("movie_name")
        year = self.data.get("year")
        prompt = f"Tell me a piece of trivia about the movie, {movie} released in {year} (DO NOT PUT ANY OTHER TEXT)"
        response = self.client.chat(
            message=prompt, 
            model=self.model,
            connectors=[{"id": "web-search",
                        }],
            temperature=1.0, 
        )

        return response.text

    