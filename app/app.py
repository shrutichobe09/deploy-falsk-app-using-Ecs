from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    data = {
        "title": "Flask Docker Application",
        "message": "Hello from ECS Flask application!",
        "emoji": "👌👌👌👌👌👌👌👌👌👌",
        "author": "Sai Teja"
    }

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)