from flask import Flask, redirect, url_for, request, app, render_template

app = Flask(__name__)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        phonenumber = request.form["phonenumber"]
        return redirect(url_for('success', name=username, mail=email, number=phonenumber))
    elif request.method == "GET":
        return render_template('login.html')

@app.route("/success/<name>/<mail>/<number>")
def success(name, mail, number):
    return f"Hello {name}. Your email is {mail} and phone is {number}"


if __name__ == '__main__':
    app.run(debug=True)
