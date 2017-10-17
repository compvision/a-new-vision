from scv import *

original = img_load('face_detect.png')  # Load the original image
faces = find_faces(original)  # Find the faces
if len(faces) != 0: # If there are faces
    x, y, width, height = faces[-1]  # Get best match for faces
    original = draw(original, img_load('greencircle.png'), x, y, width, height)
show_image(original)
close_image()
