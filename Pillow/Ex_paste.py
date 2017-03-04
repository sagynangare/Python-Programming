from PIL import Image

def main():
    fname1 = "py.png"
    
    img1 = Image.open(fname1)
    size = width, height = img1.size
    img1.paste(img1,(80,20,180,200))
    img1.show()
    del img1

if(__name__=="__main__"):

    main()
