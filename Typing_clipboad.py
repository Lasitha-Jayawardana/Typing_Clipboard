import keyboard
import time
import pyperclip

str = ""
keypress = False




while True:
    time.sleep(0.1)
    if keyboard.is_pressed("+"):
        print("start")
        
        str =pyperclip.paste()
        

        pyperclip.copy(str[0])

        while True:
               
            time.sleep(0.01)
                    
            if keypress and not keyboard.is_pressed("v"):
                    if (str):
                        pyperclip.copy(str[0])
                        print(str[0])
                        str = str[1:]
                    else:
                        print("stop")
                        break
                        
                    #beak out of while loop?
                    keypress = False
                    #break
            elif keyboard.is_pressed("v") and not keypress:
                    keypress = True
                    
            
            
            elif keyboard.is_pressed("*"):
                print("stop")
                break