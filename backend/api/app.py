from flask import Flask
from flask_cors import CORS
import json
import random
from services.movie_prompts import LLM

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return json.dumps({"text": "Backend is running!"})

@app.route("/get-movie", methods=["GET"])
def get_movie():
    year = random.randint(1997, 2005)
    llm = LLM({"year": year})
    movies = llm.parse_response()
    i = random.randint(0, 9)
    
    print(json.dumps({"text": movies[i]}))
    return json.dumps({"text": movies[i]})

if __name__ == "__main__":
    app.run(debug=True)