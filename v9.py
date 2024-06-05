from flask import Flask, abort

app = Flask(__name__)


@app.route('/<username>')
def index(username):
    if username[0].isdigit():
        abort(400)
    return f'<h1>Good Username {username}</h1>'


if __name__ == '__main__':
    app.run()

# Check username bad or good if username is bad abort 400 also Bad Request
