from flask import Flask, request
from flask_cors import CORS
import json
import random
from services.movie_descriptions import Chat
from services.movie_prompts import LLM

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return json.dumps({"text": "Backend is running!"})

# need to change to POST
@app.route("/get-movie", methods=["GET", "POST"])
def get_movie():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        year = int(data.get("year"))

        if year == None:
            return json.dumps({"error": "year not provided"})
   
        llm = LLM({"year": year})
        movies = llm.parse_response()
        i = random.randint(0, len(movies) - 1)
        print("bilal is here")
        print(i)
        
        new_data = {"movie_name": movies[i], "year": year}
        cohere_chat = Chat(new_data)

        fact = cohere_chat.ask_cohere_movie_fact()
        json_payload = {"movie_name": movies[i], "year": year, "trivia": fact}

        print(json.dumps(json_payload))
        return json.dumps(json_payload)

if __name__ == "__main__":
    app.run(debug=True)