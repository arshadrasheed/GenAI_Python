import pyautogui 
import time
import os
import pyscreeze
from datetime import datetime

pyautogui.FAILSAFE=True
pyautogui.PAUSE=1

#Press Win Key
#Search for Browser (in my case i use edge)
#Enter the Edge
#Type website

def MaximizeWindow():
    pyautogui.hotkey("alt","space")
    pyautogui.press("x")

def SearchAndEnter(appName):
    pyautogui.press("win")
    pyautogui.typewrite(appName)
    pyautogui.press("enter")

def Enter():

    pyautogui.press("enter")

def MouseMove(x,y):
    pyautogui.moveTo(x,y,duration=1)


#Main Execution
SearchAndEnter("edge")
MaximizeWindow()
time.sleep(2)
pyautogui.typewrite("www.accuweather.com")
Enter()
MouseMove(10,10)
MouseMove(740,390)
pyautogui.click()
time.sleep(1)
pyautogui.scroll(-50)
time.sleep(1)
MouseMove(10,10)
MouseMove(426,460)
pyautogui.dragTo(1115,745,duration=1)
time.sleep(1)
pyautogui.hotkey("ctrl","c")
SearchAndEnter("Excel")
MaximizeWindow()
pyautogui.hotkey("ctrl","N")
Enter()
Enter()
now= datetime.now()
formattedDate= now.strftime("%m/%d/%Y")
pyautogui.typewrite(str(formattedDate))
Enter()
pyautogui.typewrite("Today little pleasant weather")
Enter()
pyautogui.hotkey("ctrl","v")

#Fit the Cell
pyautogui.hotkey("ctrl","a")
pyautogui.hotkey("alt","h")
pyautogui.press("o")
pyautogui.press("i")
pyautogui.press("down") 


#Save the Report on Desktop
excelPath= os.path.join(os.path.expanduser("~"), "Desktop", "Demo","daily_report_2025-06-17.xlsx")
imagePath= os.path.join(os.path.expanduser("~"), "Desktop", "Demo", "daily_report_2025-06-17.png")  

time.sleep(1)
pyautogui.screenshot(imagePath)
pyautogui.hotkey("fn","f12")
pyautogui.typewrite(excelPath)
Enter()





