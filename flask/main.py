from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper_fucntion():
        f"<b>{function()}<b>"

    return wrapper_fucntion


@app.route('/')
@make_bold
def hello_world():
    return 'Hello, World!'