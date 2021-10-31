from flask import Flask


app = Flask(__name__)


@app.route('/api/home')
def home():
    return 'Home Page Route'


@app.route('/api/about')
def about():
    return 'About Page Route'


@app.route('/api/portfolio')
def portfolio():
    return 'Portfolio Page Route'


@app.route('/api/contact')
def contact():
    return 'Contact Page Route'


@app.route('/api')
def api():
    return "api"
