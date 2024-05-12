import pyautogui
import pydirectinput

cup_flag = False
off_flag = False

def check_cup():
    try:
        x, y = pyautogui.locateCenterOnScreen('cupflag.png', grayscale=True)
        global cup_flag
        cup_flag = True
        print('it is cup and home game, need to update score')
    except pyautogui.ImageNotFoundException:
        None


def check_negotiations():
    try:
        x, y = pyautogui.locateCenterOnScreen('negotiations.png', grayscale=True)
        pyautogui.click(x, y)
        global off_flag
        if off_flag:
            print('it is in negotiations, stop program')
            exit()
        else:
            print('it is in negotiations, but continue to season')
            go_match()
    except pyautogui.ImageNotFoundException:
        None  


def check_offseason():
    try:
        x, y = pyautogui.locateCenterOnScreen('offseason.png', grayscale=True)
        pyautogui.click(x, y)
        global off_flag
        if off_flag:
            print('it is in offseason, stop program')
            exit()
        else:
            print('it is in offseason, but proceed to next season')
            go_training()
    except pyautogui.ImageNotFoundException:
        None


def check_retired():
    try:
        x, y = pyautogui.locateCenterOnScreen('retired.png', grayscale=True)
        print('have players retired')
        pyautogui.hotkey('win', 'prntscrn')
    except pyautogui.ImageNotFoundException:
        None  


def check_preseason():
    try:
        x, y = pyautogui.locateCenterOnScreen('preseason.png', grayscale=True)
        print('it is preseason')
        pydirectinput.press('k')
        pydirectinput.press('n')
    except pyautogui.ImageNotFoundException:
        None  


def check_inseason():
    try:
        x, y = pyautogui.locateCenterOnScreen('inseason.png', grayscale=True)
        pyautogui.click(x, y)
        print('it is in season, will go to next match')
        global off_flag
        off_flag = True        
        go_match()
    except pyautogui.ImageNotFoundException:
        None


def go_training():
    try:
        x, y = pyautogui.locateCenterOnScreen('totraining.png', grayscale=True)
        pydirectinput.press('n')
        pydirectinput.press('n')
        pydirectinput.press('n')
        pyautogui.sleep(0.5)
        pydirectinput.press('k')
        pyautogui.sleep(0.5)
        pydirectinput.press('a')
        pydirectinput.press('a')
        pydirectinput.press('a')
        pydirectinput.press('a')
        pyautogui.sleep(0.5)
        pydirectinput.press('n')
        next_step()
    except pyautogui.ImageNotFoundException:
        print('press D to move to training')
        pydirectinput.press('d')
        pyautogui.sleep(0.25)
        check_offseason()


def go_match():
    try:
        x, y = pyautogui.locateCenterOnScreen('tonextmatch.png', grayscale=True)
        next_step()
    except pyautogui.ImageNotFoundException:
        print('press A to move to game')
        pydirectinput.press('a')
        pyautogui.sleep(0.5)
        go_match()


def next_step():
    try:
        pydirectinput.press('b') # pause game
        x, y = pyautogui.locateCenterOnScreen('match.png', grayscale=True)
        end_game()
    except pyautogui.ImageNotFoundException:
        print('press N to proceed to next stage')
        pydirectinput.press('n')
        pyautogui.sleep(0.5)
        check_inseason() # if it is in season, go to next match
        check_cup() # check if it is cup, then update score
        check_negotiations() # half or end season, need to stop program
        check_retired() # if have players retired, screenshot
        check_preseason() # if it is preseason, cancel and proceed
        check_offseason() # if it is offseason, need to stop program
        next_step()


def end_game():
    try:
        x, y = pyautogui.locateCenterOnScreen('matchover.png', grayscale=True)
        pyautogui.click(x, y)
        global cup_flag
        if cup_flag:
            x, y = pyautogui.locateCenterOnScreen('updatescore.png', grayscale=True)
            pyautogui.click(x, y)
            cup_flag = False            
        with pyautogui.hold('alt'):
            pyautogui.press('tab')
        pyautogui.sleep(0.5)
        pydirectinput.press('b') # resume game
        wait_end()
    except pyautogui.ImageNotFoundException:
        print('Error! cheat tool not open') 
    

def wait_end():
    try:
        x, y = pyautogui.locateCenterOnScreen('endgame.png', grayscale=True)
        pyautogui.click(x, y)
        next_step()
    except pyautogui.ImageNotFoundException:
        try:
            x, y = pyautogui.locateCenterOnScreen('endgame1.png', grayscale=True)
            pyautogui.click(x, y)
            next_step()            
        except pyautogui.ImageNotFoundException:
            pyautogui.sleep(12)
            pydirectinput.press('b')
            print('not in end game menu')
            wait_end()         


if __name__ =="__main__":
    check_inseason()
    check_negotiations()
    check_offseason()