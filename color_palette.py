from Pylette import extract_colors
import os

class GetColor:

    def __init__(self, file):
        self.palette = extract_colors(image=f'images/{file}', palette_size=7)
        self.most_common_color = []

        for color in self.palette:
            self.most_common_color.append(color.rgb)

        self.remove_files(file=file)

    @staticmethod
    def remove_files(file):
        os.remove(f'images/{file}')
