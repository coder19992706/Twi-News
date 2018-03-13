from flask import Flask, flash, redirect, render_template, request, session, url_for
app = Flask(__name__)

@app.route('/')
def homepage():
  return render_template('homepage.html')

@app.route('/politics')
def politics():
    return 'politics'

@app.route('/sports')
def sports():
    return 'sports'

@app.route('/entertainment')
def entertainment():
    return 'entertainment'

@app.route('/technology')
def technology():
    return 'technology'

if __name__ == '__main__':
  app.run()
