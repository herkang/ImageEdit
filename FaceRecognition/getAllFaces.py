from PIL import Image
import face_recognition
image_of_fam = face_recognition.load_image_file('family/family.png')
face_loactions=face_recognition.face_locations(image_of_fam)
for face_location in face_loactions:
    top,right,bottom,left=face_location
    face_image=image_of_fam[top:bottom,left:right]
    pil_image=Image.fromarray(face_image)
    pil_image.show()
    # pil_image.save(f"{top}.jpg")