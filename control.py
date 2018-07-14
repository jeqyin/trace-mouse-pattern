from PIL import Image
import pyautogui
import numpy as np
import keyboard
import time

time.sleep(5)
distance = 1000

while distance > 0:
    pyautogui.moveRel(distance, 0, duration=1)   # move right
    distance = distance - 50
    pyautogui.moveRel(0, distance, duration=1)   # move down
    pyautogui.moveRel(-distance, 0, duration=1)  # move left
    distance = distance - 50
    pyautogui.moveRel(0, -distance, duration=1)  # move up