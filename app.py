from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", website=["Kuttus", "Tintin"])

if __name__ == "__main__":
    app.run()