import keyboard
import time
import pyperclip

str = ""

while True:
    time.sleep(0.1)
    if keyboard.is_pressed("+"):
        print("start")
        
        str =pyperclip.paste()
        
        pyperclip.copy(str[0])
        print(str[0])
        str = str[1:]
        
        while True:
               
            time.sleep(0.1)
                    
            
            if (str):
                keyboard.press("ctrl")
                keyboard.press_and_release("v")
                keyboard.release("ctrl")
                pyperclip.copy(str[0])
                print(str[0])
                str = str[1:]
            else:
                keyboard.press("ctrl")
                keyboard.press_and_release("v")
                keyboard.release("ctrl")
                print("stop")
                
                break
                        
            if keyboard.is_pressed("*"):
                print("stop")
                break