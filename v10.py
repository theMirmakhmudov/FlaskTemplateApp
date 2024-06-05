# another port run

# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello():
#     return 'Hello, World! this application runing on 8000 port'
#
#
# if __name__ == '__main__':
#     app.run(port=8000)
# -------------------------------------------------------------------------------------------------- #
# host running flask

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World! this application runing on 192.168.0.105'


if __name__ == '__main__':
    app.run(host='192.168.0.105')
