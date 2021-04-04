from PIL import Image
img=Image.open("img_1.png")
# print(img.size)
# print(img.format)
# img.show()
area=(700,10,1200,700)
cropped_imaged=img.crop(area)

cropped_imaged.show()


