import PIL.Image
import PIL.ImageDraw
import face_recognition

# Lets start bu inputting an image and getting Python
# to recognise it
pic = face_recognition.load_image_file('shinchan.jpg')
print(pic)
face_locations = face_recognition.face_locations(pic)
print(face_locations)

# we get python to print how many faces it recognizes!
count = len(face_locations)
print("Python located {} of face(s) in this image".format(count))

# Get python to draw rectangles around images!
pil_pic = PIL.Image.fromarray(pic)
pil_pic.show()
draw_pic = PIL.ImageDraw.Draw(pil_pic)

for faces in face_locations:
    top, right, bottom, left = faces
    draw_pic.rectangle([right, bottom, left, top], outline ='green',width = '8')

pil_pic.show()


