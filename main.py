import os
import time
from flask import Flask
app = Flask(__name__)

START = time.time()

def elapsed():
    running = time.time() - START
    minutes, seconds = divmod(running, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

@app.route('/')
def root():
    return "Hello World (Python)! (up %s)\n" % elapsed()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
# import PIL
# from PIL import Image
# from tkinter.filedialog import *

# file_path = "r6.jpg"

# img = PIL.Image.open(file_path)

# myHeight, myWidth = img.size

# img = img.resize((myHeight, myWidth), PIL.Image.ANTIALIAS)

# save_path = "r6_1.jpg"
# if((os.path.getsize(file_path))>1000000):
#     print(1)
#     img.save(save_path, optimize=True,quality=25)
# else:
#     print(2)
#     img.save(save_path, optimize=True,quality=50)


