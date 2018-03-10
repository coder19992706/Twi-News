
from flask import Flask, flash, redirect, render_template, request, session, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/nikhil')
def ki():
    return render_template('index.html')

@app.route('/sudhanshu')
def hi():
    return 'This is sudhanshu'

@app.route('/prakhar')
def ji():
    return 'Hello There'

if __name__ == '__main__':
  app.run()
