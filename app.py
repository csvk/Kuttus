from flask import Flask, render_template, url_for

app = Flask(__name__)


class User:
    def __init__(self, fname, lname):
        self.fname, self.lname = fname, lname

    def initials(self):
        return "{}.{}.".format(self.fname[0], self.lname[0])


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", user=User('Souvik', 'Chanda'))

@app.route('/add')
def add():
    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)