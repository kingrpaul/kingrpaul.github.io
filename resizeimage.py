"""adapted from https://pypi.org/project/python-resize-image/"""

import math
from PIL import Image
import os

def resize_contain(image, size, resample=Image.LANCZOS, bg_color=(255, 255, 255, 0)):
    """
    Resize image according to size.
    image:      a Pillow image instance
    size:       a list of two integers [width, height]
    """
    img_format = image.format
    img = image.copy()
    img.thumbnail((size[0], size[1]), resample)
    background = Image.new('RGBA', (size[0], size[1]), bg_color)
    img_position = (
        int(math.ceil((size[0] - img.size[0]) / 2)),
        int(math.ceil((size[1] - img.size[1]) / 2))
    )
    background.paste(img, img_position)
    background.format = img_format
    return background.convert('RGBA')

large_images = [f for f in os.listdir('.') if '.jpg' in f and 'icon' not in f]
print(large_images)
for instance in large_images:
    base, ext = os.path.splitext(instance)
    print(base)
    print(ext)
    with open(instance, 'r+b') as f:
        with Image.open(f) as image:
            cover = resize_contain(image, [200, 200])
            cover.save(base + "_icon" + ext, image.format)