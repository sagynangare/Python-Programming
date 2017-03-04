from PIL import Image

def main():
    fname1 = "py.png"
    
    img1 = Image.open(fname1)
    
    img1.crop((10,10,100,100)).show()
    del img1

if(__name__=="__main__"):

    main()
