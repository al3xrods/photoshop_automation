import pyautogui
import time


rounds = int(input('How many images to edit? '))
time.sleep(8)
for i in range(rounds):
    try:
        pyautogui.hotkey('alt','ctrl','c')
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.typewrite('300')
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.typewrite('300')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.hotkey('shift', 'ctrl','N') # Create new layer
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl','backspace') # Fill new layer with white color
        time.sleep(1)    
        pyautogui.hotkey('ctrl','shift','[') # Send Backward.
        time.sleep(1)
        pyautogui.hotkey('shift','ctrl','e') # Merge Visible
        pyautogui.hotkey('ctrl','s') # Save File
        time.sleep(1)
        pyautogui.hotkey('ctrl','w') # Close File.
        time.sleep(1)
        time.sleep(1)
    except:
        pass  
    