import piexif
from PIL import Image as PILImage
from tkinter import filedialog
from tkinter import *


def main():
    filename = 'Canon_40D.jpg'
    jpeg=PILImage.open(filename)
    exif_dict = jpeg.info.get("exif")
    if exif_dict:
        exif_data = piexif.load(exif_dict)

        if piexif.ImageIFD.Orientation in exif_data["0th"]:
            print("Orientation is ", exif_data["0th"][piexif.ImageIFD.Orientation])
        if piexif.ExifIFD.Gamma in exif_data["Exif"]:
            print("Gamma is ", exif_data["Exif"][piexif.ExifIFD.Gamma])
        else:
            print("No gamma info")

    else:
        exif_bytes = 22211
        piexif.insert(exif_bytes,'pil.jpg')

def openimageDir():
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    return (root.filename)
    
if __name__== "__main__":
  main()
