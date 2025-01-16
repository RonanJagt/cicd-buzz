from flask import Flask
from buzz import generator

app = Flask(__name__)

@app.route("/")
def index():
    return f"<h1>{generator.generate_buzz()}</h1>"

if __name__ == "__main__":
    app.run()
