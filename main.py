import pyautogui
import time

message = 3
while message > 0:
    time.sleep(3)
    pyautogui.typewrite('This is a Test')
    time.sleep(1)
    pyautogui.press('enter')
    message = message - 1
