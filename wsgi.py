# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask
app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello World!", 200