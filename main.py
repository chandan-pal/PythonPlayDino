import time
import sys
import pyautogui
import keyboard
from PIL import Image, ImageGrab

mode = ""
if (len(sys.argv) > 1):
    mode = sys.argv[1]

print("Dino game is about to start in 3 secs...")
time.sleep(3)

def draw(data):
    print(str(data[99, 460]))
    for i in range(290, 350):
        for j in range(460, 480):
            data[i, j] = 0

    for i in range(290, 350):
        for j in range(390, 450):
            data[i, j] = 100

def checkCollision(data):
    for i in range(290, 350):
        for j in range(460, 480):
            if data[i, j] > 90:
                pyautogui.press('up')
                return
    
    for i in range(290, 350):
        for j in range(390, 450):
            if data[i, j] > 100:
                pyautogui.keyDown('down')
                time.sleep(0.2)
                pyautogui.keyUp('down')
                return
    return


while True:
    # take screenshot
    image = ImageGrab.grab().convert('L')

    # read image
    imageData = image.load()
    
    checkCollision(imageData)

    if "debug" == mode:
        draw(imageData)
        #print(checkCollision(imageData))
        image.show()
        break
