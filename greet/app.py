from flask import Flask

app = Flask(__name__)

GREETINGS = {
    'home': "welcome home",
    'back': "welcome back"
}

@app.route("/welcome/<gesture>")
@app.route("/welcome/", defaults={'gesture': None})
def greet(gesture):
    greeting = GREETINGS.get(gesture, "welcome")
    return greeting


