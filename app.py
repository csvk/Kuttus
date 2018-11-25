from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, flash
#from logging import DEBUG

app = Flask(__name__)
#app.logger.setLevel(DEBUG)

bookmarks = []
app.config['SECRET KEY'] = "\xb5\xab\xf2\x08fF\x08</\xa2\xceD\\\x00\x00\x8fa\x8f\xd5\xb4hY[r\xc1\xe9\x87\xb7V\xa9\xe8\xaa"


def store_bookmark(url):
    bookmarks.append(dict(
        url=url,
        user='Souvik Chanda',
        date=datetime.utcnow()
    ))


class User:
    def __init__(self, fname, lname):
        self.fname, self.lname = fname, lname

    def initials(self):
        return "{}.{}.".format(self.fname[0], self.lname[0])


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", user=User('Souvik', 'Chanda'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        url = request.form["url"]
        store_bookmark(url)
        #app.logger.debug('stored url: ' + url)
        flash('stored url: ' + url)
        return redirect(url_for('index'))

    return render_template("add.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)
