from PIL import Image
image_umn = Image.open("kang.png")
image_target = open("kang.png")
r1, g1, b1 = image_umn.split()
r2, g2, b2 = image_umn.split()
new_image = Image.merge("RGB", (r1, g2, b1))

new_image.show()
