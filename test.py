import face_recognition
image = face_recognition.load_image_file("test2.jpg")
face_locations = face_recognition.face_locations(image)
known_image = face_recognition.load_image_file("/faces/salsabil.jpg")
unknown_image = face_recognition.load_image_file(image)
biden_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
results = face_recognition.compare_faces([biden_encoding], unknown_encoding)
