from flask import  render_template
from app import app 

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return "<h1>This is the About page."