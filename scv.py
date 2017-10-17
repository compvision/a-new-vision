import cv2
from time import sleep

# Initializations
mouth_cascade = cv2.CascadeClassifier('mouth.xml')
face_cascade = cv2.CascadeClassifier('face.xml')
if mouth_cascade.empty():
  raise IOError('Unable to load the mouth cascade classifier xml file')

cap = cv2.VideoCapture(0)

def img_load(img_path):
    """
    Wrapper for cv2.imread, because we don't want the kids to have to access OpenCV directly.
    """
    return cv2.imread(img_path, -1)  # Load the image with any alphas

def draw(l_img, s_img, x_offset, y_offset, width, height):
    """
    Draws s_image on top of l_image starting at an x and y offset from the top left corner of the image, and with the
    given width and height.
    """
    s_img = cv2.resize(s_img, (width, height), interpolation = cv2.INTER_AREA)  # Resize overlay image

    # This Terrible Code was Copy Pasted Code from. OpenCV makes this really annoying but it works.:
    # http://stackoverflow.com/questions/14063070/overlay-a-smaller-image-on-a-larger-image-python-opencv
    for c in range(0,3):
        l_img[int(y_offset):int(y_offset+s_img.shape[0]), int(x_offset):int(x_offset+s_img.shape[1]), c] = s_img[:,:,c] * (s_img[:,:,3]/255.0) +  l_img[int(y_offset):int(y_offset+s_img.shape[0]), int(x_offset):int(x_offset+s_img.shape[1]), c] * (1.0 - s_img[:,:,3]/255.0)

    return l_img  # Return the drawn over background image

def show_image(img):
    cv2.imshow('Display', img)

def close_image():
    cv2.waitKey(0)

def pressed_esc():
    if cv2.waitKey(1) == 27:
        return True
    return False

def get_height(img):
    return img.shape[0]

def get_width(img):
    return img.shape[1]

# TODO: FUNCTIONS

def get_camera_image():
    ret, frame = cap.read()
    return frame

def find_mouths(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return mouth_cascade.detectMultiScale(gray, 1.7, 11)

def find_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return face_cascade.detectMultiScale(gray, 1.3, 5)
