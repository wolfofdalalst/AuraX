from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html'), 200

@app.route('/about')
def about():
    return render_template('about.html'), 200

@app.route("/github")
def githubroute():
    return redirect("https://github.com/GuptaAyush19/AuraX")

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def inernal_error():
    return render_template('500.html'), 500