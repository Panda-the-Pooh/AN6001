#
from flask import Flask
from flask import render_template, request


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # front end to back end: post
def index():
    return(render_template('index.html'))

@app.route('/main', methods=['GET', 'POST']) # front end to back end: post
def main():
    name = request.form.get('q')
    return(render_template('main.html'))

if __name__ == '__main__':
    app.run() # app.run(port=1234)