from flask import Flask, render_template, request, redirect, jsonify, send_from_directory
from os.path import abspath
from io import StringIO


app = Flask(__name__, static_folder='static')


@app.get('/')
def send_file():
    return jsonify({"message": "some text"})


@app.route('/file')
def get_file():
    filepath = abspath('./first.zip')
    return send_from_directory(app.static_folder, 'first.zip')


@app.route('/pdf')
def get_pdf():
    filepath = abspath('./dbms.pdf')
    return send_from_directory(app.static_folder, 'dbms.pdf')


if __name__ == '__main__':
    app.run()
