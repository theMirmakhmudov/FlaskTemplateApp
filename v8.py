from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("login.html")


@app.route('/success')
def success():
    return "Muvaffaqiyatli ro'yhatdan o'tdingiz xurmatli admin!"


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST" and request.form["username"] == "admin" and request.form["username"] == "mirmakhmudov16":
        return redirect(url_for("success"))

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
