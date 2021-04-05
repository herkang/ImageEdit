from PIL import Image
from PIL import ImageFilter
image_umn = Image.open("kang.png")
# black_white=image_umn.convert("L")
# black_white.show()
# blur_kang=image_umn.filter(ImageFilter.BLUR)
# blur_kang.show()
# detail=image_umn.filter(ImageFilter.DETAIL)
# detail.show()
edges = image_umn.filter(ImageFilter.FIND_EDGES)
edges.show()

