from flask import Flask
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return json.dumps({
  "link": "https://giphy.com/embed/SKGo6OYe24EBG"
    })

if __name__ == "__main__":
    app.run(debug=True)