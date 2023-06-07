import os
import time
import pyautogui

class cleanAll:
    def tasks():
        os.system('taskkill /f /im explorer.exe')
        time.sleep(3)
        os.system('start explorer.exe')
    def tmp():
            try:
                tmp_path = 'C:\Windows\Temp'
                os.system(f'start explorer.exe {tmp_path}')
                time.sleep(3)
                pyautogui.hotkey("ctrlleft", "a")
                pyautogui.hotkey("delete")
                pyautogui.press('enter')
                time.sleep(5)
                cleanAll.tasks()

            except ValueError:
                pass
    def user_tmp(): 
            try:
                pyautogui.hotkey('win','r')
                pyautogui.typewrite('%temp%')
                pyautogui.press('enter')
                time.sleep(3)
                pyautogui.hotkey("ctrlleft", "a")
                pyautogui.hotkey("delete")
                pyautogui.press('enter')
                time.sleep(5)
                cleanAll.tasks()
            except ValueError:
                pass
    def prefetch():
            try:
                pyautogui.hotkey('win','r')
                pyautogui.typewrite('prefetch')
                pyautogui.press('enter')
                time.sleep(3)
                pyautogui.hotkey("ctrlleft", "a")
                pyautogui.hotkey("delete")
                pyautogui.press('enter')
                time.sleep(5)
                cleanAll.tasks()
            except ValueError:
                pass
    def cleanRCB():
        os.system('start shell:RecycleBinFolder')
        time.sleep(3)
        pyautogui.hotkey("ctrlleft", "a")
        pyautogui.hotkey("delete")
        pyautogui.press('enter')
        time.sleep(5)
        cleanAll.tasks()

while True:
    print('''
        ===============
          Menu cleanup
        ===============
        [1] Clean All
        [2] Exit

        
        ''')
    menu_ = input('\ncutemi@debugpoint~# ')
    if menu_ == '1':
            cleanAll.tmp()
            cleanAll.user_tmp()
            cleanAll.prefetch()
            cleanAll.cleanRCB()
    elif menu_ == '2':
            os.system('cls')
            print('''
            ▌ ▌▞▀▖▛▀▖▛▀▖▌ ▌ ▙ ▌▜▘▞▀▖▛▀▘ ▛▀▖▞▀▖▌ ▌ ▐
            ▙▄▌▙▄▌▙▄▘▙▄▘▝▞  ▌▌▌▐ ▌  ▙▄  ▌ ▌▙▄▌▝▞  ▐
            ▌ ▌▌ ▌▌  ▌   ▌  ▌▝▌▐ ▌ ▖▌   ▌ ▌▌ ▌ ▌  ▝
            ▘ ▘▘ ▘▘  ▘   ▘  ▘ ▘▀▘▝▀ ▀▀▘ ▀▀ ▘ ▘ ▘  ▝



            ''')
            os.system('timeout /t 10 /nobreak')
            exit()







