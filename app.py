from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/articles")
def articles():
   return render_template("articles.html")


@app.route("/contact")
def contact():
   return render_template("contact.html")

@app.route("/documentaries")
def documentaries():
   return render_template("documentaries.html")



if __name__=="__main__":
    app.run(debug=True)

