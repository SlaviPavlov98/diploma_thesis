import cv2
import easygui
import sys
import platform


# Function to get the OS
def get_os():
    os = platform.system()
    return os


# Function to get a filepath for a given directory
def get_file_path():
    file_path = easygui.diropenbox(msg="Choose where to save the sketch(It will be named sketch.jpg)")
    return file_path


# Function to build the save file path depending on the os
def build_save_file_path(file_path):
    os = get_os()
    if os == 'Windows':
        file_path += "\\sketch.jpg"
    #elif os == 'Linux':
    #    file_path += "/sketch.jpg"
    else:
        easygui.msgbox(msg='Issue detecting OS')
        cv2.waitKey(0)
        sys.exit()
    return file_path


# Function which asks the user if he wishes to save the new sketch
def should_i_save():
    answer = easygui.ynbox(msg='Do you wish to save the sketch?')
    return answer


# It can open any file but if it's not an image the next function would throw an exception
def get_image_file():
    file = easygui.fileopenbox(msg="Choose a picture to be sketched(*.jpg or *.png)", filetypes=['*.png', '*.jpg'])
    file = cv2.imread(file)
    return file


# Function which saves the new file
def save_image(image):
    file_path = get_file_path()
    save_file_path = build_save_file_path(file_path)
    cv2.imwrite(save_file_path, image)


# Function to create the sketch
def create_sketch(image):
    try:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        inverted_image = 255 - gray_image
        blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
        inverted_blurred = 255 - blurred
        sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    except cv2.error:
        print("You have not chosen a valid file! Please use *.jpg or *.png images")
        sys.exit()
    return sketch


# Loads the image and shows the sketch. Fails if not a valid image file is passed
def show_sketch(sketch):
    cv2.imshow("Sketch", sketch)
    cv2.waitKey(0)


# Execution
def main():
    image = get_image_file()
    sketch = create_sketch(image)
    show_sketch(sketch)
    if should_i_save():
        save_image(sketch)


main()
