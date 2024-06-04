from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, I'm Flask"

@app.route('/hello')
def say_hello():
    return "Hello World"


if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(debug=True)





