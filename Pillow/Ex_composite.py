from PIL import Image

def main():
    fname1 = "py.png"
    fname2 = "mess.png"
    img1 = Image.open(fname1)
    img2 = Image.open(fname2)

    Image.composite(img1, img2, img1)

    del img1,img2


if(__name__=="__main__"):

    main()
