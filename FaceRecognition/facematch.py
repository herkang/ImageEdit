import face_recognition

image_of_kang = face_recognition.load_image_file('known_face/kang/kang.png')
kang_face_encoding = face_recognition.face_encodings(image_of_kang)[0]
unknown_image = face_recognition.load_image_file(
    'unknownface/img.png')
unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

# unknown_image = face_recognition.load_image_file(
#     'unknownface/DuaLipa.jpeg')
# unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare faces
results = face_recognition.compare_faces(
    [kang_face_encoding], unknown_face_encoding)

if results[0]:
    print('Yee,This is Kang for real')
else:
    print('Sorry this is not kang')