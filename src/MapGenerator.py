__author__ = 'Gene'

import operator
from PIL import Image

def generate(file, weights, iteration, mutation_rate):
    width = file.size[0]
    height = file.size[1]
    image = file.load()
    for t in range(iteration):
        for h in range(height):
            for w in range(width):
                pixel = image[w, h]
                pixel = (int(x * weights[4]) for x in pixel)
                if h - 1 >= 0:
                    north_pixel = (int(x * weights[0]) for x in image[w, h - 1])
                    pixel = tuple(map(operator.add, pixel, north_pixel))
                if h + 1 < height:
                    south_pixel = (int(x * weights[2]) for x in image[w, h + 1])
                    pixel = tuple(map(operator.add, pixel, south_pixel))
                if w - 1 >= 0:
                    west_pixel = (int(x * weights[3]) for x in image[w - 1, h])
                    pixel = tuple(map(operator.add, pixel, west_pixel))
                if w + 1 < width:
                    east_pixel = (int(x * weights[1]) for x in image[w + 1, h])
                    pixel = tuple(map(operator.add, pixel, east_pixel))
                image[w, h] = pixel
                #print(pixel)
        print(t)
    return file

out = generate(Image.open("C:/Users/Gene/Desktop/seed.png"), (.2, .2, .2, .2, .2), 50, 0)
out.save("map.png", "png")