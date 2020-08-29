import pyautogui
import time
while True:
    time.sleep(4)
    pyautogui.typewrite('This is a Test')
    time.sleep(1)
    pyautogui.press('enter')