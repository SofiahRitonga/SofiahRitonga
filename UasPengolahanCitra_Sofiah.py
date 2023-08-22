from turtle import width
import PIL
from PIL import Image
from tkinter.filedialog import *

path = askopenfilename()
img = PIL.Image.open(path)
height, width = img.size

img = img.resize((height, width), PIL.image.ANTIALIAS)
save_path = asksaveasfilename()

img.save(save_path + "_compressed.JPEG")
