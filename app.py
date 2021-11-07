from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

def readme():
    import requests
    from bs4 import BeautifulSoup

    page = requests.get('https://github.com/GuptaAyush19/AuraX/blob/develop/README.md')
    soup = BeautifulSoup(page.content, 'html.parser') 

    return soup.find(id='readme')

@app.route('/')
def index():
    return render_template('index.html'), 200

@app.route('/about')
def about():
<<<<<<< HEAD
    return render_template('about.html'), 200
=======
    return render_template('about.html', about=readme()), 200
>>>>>>> 661d80d3aea57d3e813f16b5adc2db3677bae7fe

@app.route("/github")
def githubroute():
    return redirect("https://github.com/GuptaAyush19/AuraX")

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
<<<<<<< HEAD
def inernal_error():
    return render_template('500.html'), 500
=======
def internal_error():
    return render_template('500.html'), 500
>>>>>>> 661d80d3aea57d3e813f16b5adc2db3677bae7fe
