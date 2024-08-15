import pyautogui
import webbrowser
import time
print('''
      THis is initial version of auto chat bot by nirvik nepal
      copyright@nirviknepal
      ''')
try :

    webbrowser.open("www.instagram.com")
    time.sleep(7)
    username_x,username_y = 1133,415 #input your location by runninf the position.py
    password_x,password_y = 1102,471    #input your location by running the position.py
    login_x,login_y = 1197,518
    pyautogui.click(username_x,username_y)
    time.sleep(1)
    pyautogui.typewrite("User_name")
    pyautogui.click(password_x,password_y)
    time.sleep(1)
    pyautogui.typewrite("Password@1124")
    time.sleep(1)
    pyautogui.click(1197,518)
    # pyautogui.scroll()
except Exception as e : 
    print("Error has occured ",e )