from flask import Flask, render_template, request, redirect, url_for
from flask_dropzone import Dropzone
from color_palette import GetColor
from flask_socketio import SocketIO
import json
import os

app = Flask(__name__)
socketio = SocketIO(app)


# plugins
dropzone = Dropzone(app)
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = '.jpg, .jpeg, .png, .bmp, .tiff, .webp'
app.config['DROPZONE_PREVIEW_WIDTH'] = 256
app.config['DROPZONE_PREVIEW_HEIGHT'] = 256
app.config['DROPZONE_MAX_FILE_SIZE'] = 8


@socketio.on('connect')
def handle_connect():
    print('User connected')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.files:
            file = request.files.get('file')
            file.save(os.path.join('images', file.filename))
            img_colors = GetColor(file=file.filename)
            colors = [item.tolist() for item in img_colors.most_common_color]

            socketio.emit('common_colors', {'colors': [colors]})

    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app, debug=True)
