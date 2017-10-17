from scv import *

stache = img_load('stache.png')  # Load the stache
while True:
    original = get_camera_image()  # Load the original image
    mouths = find_mouths(original)  # Find the mouths

    if len(mouths) != 0: # If there are mouths
        x, y, width, height = mouths[-1]  # Get best match for mouth
        original = draw(original, stache, x, int(y-height/3.5), width, int(height/1.2))

    show_image(original)

    if pressed_esc():
        break
