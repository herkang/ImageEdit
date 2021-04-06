import face_recognition
image=face_recognition.load_image_file('family/family.png')
face_locations=face_recognition.face_locations(image)
#gives array of coord of each face
print(face_locations)
print(f"There are {len(face_locations)} people in this image ")
