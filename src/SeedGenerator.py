__author__ = 'Gene'

import PIL
from PIL import Image
import random

def generate_random_seed(width, height, out_file_name):
    file = Image.new("RGB", (width, height), 0)
    for i in range(height):
        for j in range(width):
            file.putpixel((i,j),(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    file.save(out_file_name, "PNG")

def generate_random_seed(width, height, out_file_name):
    file = Image.new("RGB", (width, height), "white")
    file.save(out_file_name, "PNG")