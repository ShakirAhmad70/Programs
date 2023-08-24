import pyautogui
import time

def rotate_screen(degrees):
    pyautogui.hotkey('ctrl', 'alt', 'shift')
    time.sleep(1)  # Give some time for the rotation key combination to take effect
    pyautogui.press(str(degrees))

# Example usage: rotate the screen by 90 degrees clockwise
rotate_screen(90)