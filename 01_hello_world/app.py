from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def index():
    username = request.args.get("username")
    return render_template("index.html", username=username)


@app.route("/<username>")
def index_by_username(username):
    return render_template("index.html", username=username)


if __name__ == "__main__":
    app.run()
