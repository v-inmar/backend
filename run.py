from flask import Flask
import os

app = Flask(__name__)

@app.route('/test')
def test():
    return "<h1>Hello World</h1>"

if __name__ == "__main__":
    app.run(host=os.getenv("IP", "0.0.0.0"), port=os.getenv("PORT", 5000), debug=True)