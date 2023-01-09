import cv2
import pyautogui
import time
import mobs
import keyboard

btnready = pyautogui.locateOnScreen('readybtn.png')


piedra = pyautogui.locateOnScreen(mobs.piedra)

rangescreen = (0, 0, 1000, 300)

def moveto(x,y):
    pyautogui.moveTo(x,y)

print('Starting in 3 seconds...')
time.sleep(3)


def checklanding():
    print('Checking if ready button is on screen...')
    if btnready != None:
        pyautogui.moveTo(btnready)
        pyautogui.click()
        time.sleep(1)
        print('Ready button found. Clicking...')
    else:
        print('Ready button not found, passing...')
        pass


def checkmob():
    for mob in mobs.mobslist:
        mobisonscreen = False
        while mobisonscreen == False:
            try:
                mob = pyautogui.locateOnScreen(mob, region = rangescreen)
                print('Checking if ' + mob + ' is on screen...')
                if mob != None:
                    print('{mob} found, moving to it...').format(mob = mob)
                    pyautogui.moveTo(mob)
                    time.sleep(0.5)
                    mobisonscreen = True
                else:
                    print('{mob} killed or not found, passing...').format(mob = mob)
                    pyautogui.locateOnScreen('player.png')
            except:
                pass
        
def movement():
    pyautogui.moveTo(500, 500)
    time.sleep(0.5)
    pyautogui.moveTo(500, 100)
    time.sleep(0.5)
    pyautogui.moveTo(100, 100)
    time.sleep(0.5)
    pyautogui.moveTo(100, 500)
    
    

while True and keyboard.is_pressed('q') == False:
    checklanding()
    #checkmob()
    movement()
    