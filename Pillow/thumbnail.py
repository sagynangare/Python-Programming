from PIL import Image
from PIL import ImageFilter

def main():
    fname1 = "py.png"
    
    img1 = Image.open(fname1)
    size = width, height = img1.size
    img1.thumbnail((128,128), Image.NEAREST)

 
    img1.show()
    del img1

if(__name__=="__main__"):

    main()
