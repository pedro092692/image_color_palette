from flask import Flask, render_template, request, redirect, url_for
from flask_dropzone import Dropzone

app = Flask(__name__)

# plugins
dropzone = Dropzone(app)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
