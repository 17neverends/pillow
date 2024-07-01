from PIL import Image
import numpy as np


class ImageProcessor:
    def __init__(self, image_path, block_size=12, colors=None):
        self.image_path = image_path
        self.block_size = block_size
        self.colors = colors if colors is not None else [
            (50, 50, 50),
            (75, 75, 75),
            (110, 110, 110),
            (170, 170, 170),
            (205, 205, 205)
        ]
        self.image = self.load_image()
        self.image_array = np.array(self.image)

    def load_image(self):
        image = Image.open(self.image_path)
        return image.convert('L')

    @staticmethod
    def closest_color(value, colors):
        return min(colors, key=lambda color: abs(color[0] - value))

    def process_block(self, block):
        avg_color = np.mean(block)
        color = self.closest_color(avg_color, self.colors)
        return color[0]

    def process_image(self):
        for i in range(0, self.image_array.shape[0], self.block_size):
            for j in range(0, self.image_array.shape[1], self.block_size):
                block = self.image_array[i:i+self.block_size, j:j+self.block_size]
                color = self.process_block(block)
                self.image_array[i:i+self.block_size, j:j+self.block_size] = color

    def save_image(self, output_path):
        image = Image.fromarray(self.image_array.astype('uint8'))
        image.save(output_path)


def main():
    image_path1 = 'input.jpg'
    output_path1 = 'output.jpg'
    block_size = 10
    processor = ImageProcessor(image_path1, block_size)
    processor.process_image()
    processor.save_image(output_path1)


if __name__ == "__main__":
    main()
