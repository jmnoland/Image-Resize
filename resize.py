from PIL import Image
import numpy as np

def resize(filePath, scale):
    _scale = lambda dim, s: int(dim * s / 100)
    im = Image.open(filePath)
    return im.resize(scale)
