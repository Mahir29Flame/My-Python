import os, sys
from PIL import Image

with Image.open("image.jpg") as img:
    img.show()