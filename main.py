from flask import Flask
app = Flask(__name__)


def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/bye')
@bold
def bye():
    return 'bye!'


@ app.route('/<path:name>')
def say_nice(name):
    return f"Hello {name}"


if __name__ == "__main__":
    app.run(debug=True)
