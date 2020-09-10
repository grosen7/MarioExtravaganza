from flask import Flask, render_template, request, url_for, flash, redirect, Response, session, send_from_directory
from flask_bootstrap import Bootstrap
import os
from app import app
from app.classes.MarioExtravaganza import MarioExtravaganza

Bootstrap(app)
app.secret_key = "secret"
# app.secret_key = os.environ["SECRET"]

## MAIN PAGE
@app.route("/", methods = ["GET", "POST"])
def main():
    if request.method == "POST":
        try:
            # try to build object and get file download data
            # to return to user
            marioObj = MarioExtravaganza()
            fileData = marioObj.process(request)
            download = Response(fileData, mimetype = "text/csv")
            download.headers.set("Content-Disposition", "attachment", filename="racelineups.csv")
        except Exception as e:
            # redirect to error page if error is encountered
            flash(str(e))
            return redirect(url_for("error"))

        return download

    return render_template("main.html", title = "Mario Kart Extravaganza")

##ERROR PAGE
@app.route("/error", methods = ["GET", "POST"])
def error():
    # return to main page if post request
    if request.method =='POST':
        return redirect(url_for('main'))
    return render_template('error.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
