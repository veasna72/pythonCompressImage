import os
import PIL
from PIL import Image
#from tkinter.filedialog import *

file_path = "r6.jpg"

img = PIL.Image.open(file_path)

myHeight, myWidth = img.size

img = img.resize((myHeight, myWidth), PIL.Image.ANTIALIAS)

save_path = "r6_1.jpg"
if((os.path.getsize(file_path))>1000000):
    print(1)
    img.save(save_path, optimize=True,quality=25)
else:
    print(2)
    img.save(save_path, optimize=True,quality=50)
