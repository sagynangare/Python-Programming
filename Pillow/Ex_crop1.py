from PIL import Image
from PIL import ImageFilter
def main():
    fname1 = "py.png"
    
    img1 = Image.open(fname1)
    size = width, height = img1.size;
    coordinate = x,y = 180, 69
    img1.filter(ImageFilter.EDGE_ENHANCE).show()
    print list(img1.getdata())
    del img1

if(__name__=="__main__"):

    main()
