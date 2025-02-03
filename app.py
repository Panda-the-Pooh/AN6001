#
from flask import Flask
from flask import render_template, request
import textblob
import os
import google.generativeai as genai

api = os.getenv('makersuite')
genai.configure(api_key = api)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST']) # front end to back end: post
def index():
    return(render_template('index.html'))

@app.route('/main', methods=['GET', 'POST']) # front end to back end: post
def main():
    name = request.form.get('q')
    return(render_template('main.html'))

@app.route('/SA', methods=['GET', 'POST']) # front end to back end: post
def SA():
    return(render_template('SA.html'))

@app.route('/SA_result', methods=['GET', 'POST']) # front end to back end: post
def SA_result():
    q = request.form.get('q') # former q - backend, latter q - frontend
    r = textblob.TextBlob(q).sentiment # r - backend
    return(render_template('SA_result.html', r=r)) # former r - frontend, latter r - backend

@app.route('/genAI', methods=['GET', 'POST']) # front end to back end: post
def genAI():
    return(render_template('genAI.html'))

@app.route('/genAI_result', methods=['GET', 'POST'])
def genAI_result():
    q = request.form.get('q')
    r = model.generate_content(q)
    return(render_template('genAI_result.html', r=r.candidates[0].content.parts[0].text))

@app.route('/paynow', methods=['GET', 'POST'])
def paynow():
    return(render_template('paynow.html'))

if __name__ == '__main__':
    app.run() # app.run(port=1234)