from PIL import Image
image_umn = Image.open("kang.png")
black_white=image_umn.convert("L")
black_white.show()
