from PIL import Image

def main(  ):
    size = width, height = 320,240
    image = Image.new("RGB", size, "orange")
    image.show()
    del image

if(__name__ == "__main__"):
    main()

