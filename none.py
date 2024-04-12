import time
import os
import keyboard


os.system('cls')
with open('text.txt', 'r', encoding='utf-8') as text:
    try:
        for i in text:
            time.sleep(3)
            keyboard.write(i)
    except:
        print('erorr')
