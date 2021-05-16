import pyautogui
import time

print(pyautogui.size())
time.sleep(3)


print(pyautogui.position())
pyautogui.moveTo(406,31)
pyautogui.click()

pyautogui.moveTo(424,58)
pyautogui.click()

#closing the preferences.
pyautogui.moveTo(1455,712,3)
pyautogui.click()


#Opening menue with keyboard shortcuts.
pyautogui.hotkey('alt','t')
time.sleep(2)
pyautogui.press('escape')
pyautogui.press('escape')


#NOTE: To get the co ordinates of an object start the cmd terminal with python
#import the pyautogui module
#run pyautoqui.displayMousePosition()
# press ctrl + C to exit.