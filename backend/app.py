from flask import Flask
app = Flask(__name__)


@app.route('/')
def getjobs():
    return 'Hello, World!'
