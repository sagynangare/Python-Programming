from PIL import Image

def main():
    fname1 = "py.png"
    
    img1 = Image.open(fname1)
    
    img1.convert("L").show()
    del img1

if(__name__=="__main__"):

    main()
