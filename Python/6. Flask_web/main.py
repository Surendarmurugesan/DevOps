from flask import Flask, redirect, render_template, url_for
import datetime

today=datetime.datetime.today()
print(f"{today:%B %d, %Y}")
#print(f"{today}")      ## Check the today o/p.It's working

appli = Flask(__name__)

@appli.route("/<name>")
def home(name):
    return render_template("index.html", content=["AB", "Virat"])

#@appli.route("/<name>")
#def user(name):
#    return f"Hello {name}"
#   f = The idea behind f-strings is to make string interpolation simpler. To create an f-string, prefix the string with the letter “ f ”. The string itself can be formatted in much the same way that you would with str.format().

@appli.route("/admin")
def admin():
    return redirect(url_for("home"))

if __name__ == "__main__":
    appli.run()