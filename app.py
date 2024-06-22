from flask import Flask, render_template
from datetime import date

app = Flask(__name__)


@app.route("/")
def home():
    today = str(date.today())
    return render_template("index.html", time_stamp=today)


@app.route("/articles")
def articles():
    today = str(date.today())
    return render_template("articles.html", time_stamp=today)


@app.route("/contact")
def contact():
    today = str(date.today())
    return render_template("contact.html", time_stamp=today)

@app.route("/documentaries")
def documentaries():
    today = str(date.today())
    return render_template("documentaries.html", time_stamp=today)



if __name__=="__main__":
    app.run(debug=True)

