from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

today = str(date.today())

@app.route("/")
def home():
    return render_template("index.html", time_stamp=today)


@app.route("/articles")
def articles():
    return render_template("articles.html", time_stamp=today)


@app.route("/contact")
def contact():
    return render_template("contact.html", time_stamp=today)

@app.route("/documentaries")
def documentaries():
    return render_template("documentaries.html", time_stamp=today)



if __name__=="__main__":
    app.run(debug=True)

