from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

@app.route('/nikhil')
def ki():
    return 'Nikhil Bansal'

@app.route('/sudhanshu')
def hi():
    return 'This is sudhanshu'

@app.route('/prakhar')
def ji():
    return 'Hello There'

if __name__ == '__main__':
  app.run()
