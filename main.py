import numpy
from PIL import Image
from fxpmath import Fxp
import sys

file1 = open("empty-heart.hex", "w")
def get_image(image_path):
    """Get a numpy array of an image so that one can access values[x][y]."""
    image = Image.open(image_path, "r")
    width, height = image.size
    pixel_values = list(image.getdata())
    if image.mode == "RGB":
        channels = 3
    elif image.mode == "L":
        channels = 1
    else:
        print("Unknown mode: %s" % image.mode)
        return None
    pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
    return pixel_values, width, height
image, x, y = get_image("empty-heart.jpg")

file1.write('v2.0 raw')
for j in range(y):
    for i in range(x):
       #print (image[i][j] >> 4)
       fxppixel = Fxp(image[j][i] , 0, 24, 0)
       fxppixel = Fxp(fxppixel >> 4, 0, 4, 0)

       print(str(fxppixel.hex()).replace("0x", ""))

       tempstr = str(fxppixel.hex()).replace("0x", "")
       tempstr = tempstr.replace("'", "")
       tempstr = tempstr.replace("[", "")
       tempstr = tempstr.replace("]", "")
       tempstr = tempstr.replace(",", "")
       tempstr = tempstr.replace(" ", "")



       file1.write('\n' + tempstr)
       #file1.write('\n' + str(image[j][i] >> 4))
file1.close()