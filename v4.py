from flask import Flask

app = Flask(__name__)


@app.route('/hello/<your_name>')
def hello_your_name(your_name):
    return 'Hello %s!' % your_name


if __name__ == '__main__':
    app.run(debug=True)

# 127.0.0.1:5000/hello/YOUR_NAME
