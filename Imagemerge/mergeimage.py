from PIL import Image
image_umn=Image.open("img_1.png")
r , g ,b=image_umn.split()
r.show()
g.show()
b.show()
