from PIL import Image
kang=Image.open("kang.png")
square_kang=kang.resize((300,300))
flip_kang=kang.transpose(Image.FLIP_TOP_BOTTOM)
flip_kang.show()
spin_kang=kang.transpose(Image.ROTATE_270)
spin_kang.show()

