import time
import keyboard
import pyautogui
import pyperclip
from pyscreeze import ImageNotFoundException

songs = []
def getdeadsongs(x1, y1, x2, y2):
    nr = 1
    while True:
        if keyboard.is_pressed('q'):
            break
        try:
            for loc in pyautogui.locateAllOnScreen('x.jpg',region=(x1, y1, x2, y2), confidence=0.6):
                point = pyautogui.center(loc)
                x, y = point

                pyautogui.click(x, y, button='right')

                time.sleep(0.1)
                copy = pyautogui.locateOnScreen('copy.jpg', confidence=0.8)
                point = pyautogui.center(copy)
                x, y = point
                pyautogui.click(x, y)
                text = pyperclip.paste()
                songname = text.split('\t')[0]
                songs.append(songname)
                print(songname)
                nr += 1
        except ImageNotFoundException:
            print("No more songs found")
        pyautogui.press('pagedown')

while True:
    pyautogui.PAUSE = 0.5
    if keyboard.is_pressed('esc'):
        break
    if keyboard.is_pressed('f5'):
        x1, y1 = pyautogui.position()
        print("X1, Y2: {}, {}1".format(x1, y1))
    if keyboard.is_pressed('f6'):
        x2, y2 = pyautogui.position()
        print("X2, Y2: {}, {}1".format(x2, y2))

getdeadsongs(x1, y1, x2, y2)

print("Songs found:")
with open('deadtunes.txt', 'w') as f:
    for item in songs:
        f.write("%s\n" % item)
        print(item)