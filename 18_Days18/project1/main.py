import colorgram
from PIL import Image
import numpy as np


img = Image.open('image.jpg').convert('RGB')
pixels = np.array(img).reshape(-1, 3)
unique_count = len(np.unique(pixels, axis=0))

# extract warna dari image
colors = colorgram.extract('image.jpg', unique_count)
total = len(colors)
rgb_color = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_format_color = (r, g, b)
    rgb_color.append(new_format_color)

print(rgb_color)
print('\n' * 3)
print(f'Total warna {total}')