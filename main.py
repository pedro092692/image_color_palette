from flask import Flask, render_template, request, redirect, url_for
from flask_dropzone import Dropzone
from color_palette import GetColor
from flask_socketio import SocketIO
import os

app = Flask(__name__)
socketio = SocketIO(app)


# plugins
dropzone = Dropzone(app)
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = '.jpg, .jpeg, .png, .bmp, .tiff, .webp, .svg'
app.config['DROPZONE_MAX_FILE_SIZE'] = 8


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.files:
            file = request.files.get('file')
            file.save(os.path.join('images', file.filename))
            img_colors = GetColor(file=file.filename)

    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, debug=True)
