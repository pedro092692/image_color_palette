from Pylette import extract_colors


class GetColor:

    def __init__(self):
        self.palette = extract_colors(image='demo.png', palette_size=7)
        self.most_common_color = []

        for color in self.palette:
            self.most_common_color.append(color.rgb)

        print(self.most_common_color)



