from flask import Flask

app = Flask(__name__)


def say_hello():
    return "Hello Flask"


def say_bye():
    return "Bye Flask"


app.add_url_rule('/', 'hello', say_hello)
app.add_url_rule('/hello','')

if __name__ == "__main__":
    app.debug = True
    app.run()
    app.run(debug=True)
