from PIL import Image
from PIL import ImageFilter

baby = Image.open('C:\Users\KOUSHAL\Desktop\Sagar Python\practice program\Chavanwadi.jpg')
edges = baby.filter(ImageFilter.FIND_EDGES)
baby.show()
edges.show()
