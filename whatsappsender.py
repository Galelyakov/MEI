import numbers
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.common.keys import Keys
import pyautogui                                                                                 
import time 
numbers = ['550000000']

print("Starting Auto Sender/n")
time.sleep(5)
pyautogui.hotkey('ctrl','t')                              
for i in range(len(numbers)):
    link ='https://wa.me/972' + numbers[i]
    pyautogui.typewrite(link)       
    pyautogui.press('enter')
    time.sleep(5)                                                                                               
    pyautogui.press('tab',presses=8)
    pyautogui.press('enter')                                
    time.sleep(5)
    pyautogui.press('tab', presses=2)
    pyautogui.press('enter')
    time.sleep(12)
    print("Sending New Msg")
    pyautogui.hotkey('ctrl' , 'v')
    pyautogui.press('enter')
    print(593     )
    time.sleep(5)
    print("Finsh")
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    pyautogui.keyUp('ctrl')
    time.sleep(3)
    pyautogui.write(['f6'])
    time.sleep(1)
