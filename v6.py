from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/square', methods=['GET'])
def squarenumber():

    if request.method == 'GET':

        if (request.args.get('num') == None):
            return render_template('squarenum.html')

        elif (request.args.get('num') == ''):
            return "<html><body> <h1>Invalid number</h1></body></html>"

            number = request.args.get('num')
            sq = int(number) * int(number)

            return render_template('answer.html',
                                   squareofnum=sq, num=number)


# Start with flask web app with debug as
# True only if this is the starting page
if (__name__ == "__main__"):
    app.run(debug=True)
