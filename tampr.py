#imports
import piexif
from PIL import Image as PILImage
from tkinter import filedialog
from tkinter import *
from PIL import Image, ExifTags
from tkinter import ttk
from tkinter import messagebox

root = Tk()
def main():
    img = Image.open(openimageDir()) #open the file 
    #get EXIF data from the file  
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS } #Got from StackOVerflow, for how to extract tags 

	#pop up with the message box
    answer = messagebox.askquestion("Welcome to Tampr System! ","Would you like to modify the Metadata?")

    if answer == "no":
        showData(exif)
    else:
        editData(img)
    

    #File browser Window
def openimageDir():
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    return (root.filename)
#If user selects yes
def editData(img):
    exif_dict = piexif.load(img.info['exif'])
    print(piexif.ExifIFD.DateTimeOriginal)
#Actual change to metadata
    zeroth_ifd = {
        piexif.ImageIFD.Artist: u"Jon And Greg",
        piexif.ImageIFD.XResolution: (96, 1),
        piexif.ImageIFD.YResolution: (96, 1),
        piexif.ImageIFD.Software: u"Tampr"
    }

    exif_ifd = {
        piexif.ExifIFD.DateTimeOriginal: u"2020:09:29 10:10:10",
        piexif.ExifIFD.LensMake: u"Canon",
        piexif.ExifIFD.Sharpness: 1,
        piexif.ExifIFD.LensSpecification: ((1, 1), (1, 1), (1, 1), (1, 1)),
    }
#Save as new image file 
    exif_dict = {"0th": zeroth_ifd, "Exif": exif_ifd}
    exif_bytes = piexif.dump(exif_dict)

    exif_bytes = piexif.dump(exif_dict)
    img.save("out.jpg", exif=exif_bytes)
    print("Data modified, output file out.jpg")
#Show the table of metadata with a scrollbar
def showData(exif):
    
    for key_name in exif:
        print ((str(key_name),  str(exif[key_name])))

    frame = Frame(root)
    frame.pack()
    tree = ttk.Treeview(frame, columns = (1,2), height = 40, show = "headings")
    tree.pack(side = 'left')
    
    tree.column("1", width=150)
    tree.column("2", width=150)
    tree.heading("1", text="TAG")
    tree.heading("2", text="VALUE")

 #Scrollbar
    scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scroll.pack(side = 'right', fill = 'y')
    tree.configure(yscrollcommand=scroll.set)

    for key_name in exif:
        tree.insert("", 'end', values=(str(key_name),str(exif[key_name])))

    

    root.mainloop()
if __name__== "__main__":
  main()
