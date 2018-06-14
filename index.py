from flask import Flask,render_template
from sentiment import Sentiments

app = Flask(__name__)

Sentiments = Sentiments()

@app.route("/")
def hello():
    return render_template('home.html',sentiments = Sentiments)


if __name__ == '__main__':
    app.run(debug=True)