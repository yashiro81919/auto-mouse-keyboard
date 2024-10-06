import pyautogui
import pydirectinput

cup_flag = False
off_flag = False

def check_cup():
    try:
        x, y = pyautogui.locateCenterOnScreen('cupflag.png')
        pyautogui.click(x, y)
        print('it is cup and home game')
        return True
    except pyautogui.ImageNotFoundException:
        return False


def check_negotiations():
    try:
        x, y = pyautogui.locateCenterOnScreen('negotiations.png')
        pyautogui.click(x, y)
        print('it is in negotiations')
        return True
    except pyautogui.ImageNotFoundException:
        return False  


def check_offseason():
    try:
        x, y = pyautogui.locateCenterOnScreen('offseason.png')
        pyautogui.click(x, y)
        print('it is in offseason')
        return True
    except pyautogui.ImageNotFoundException:
        return False  


def check_retired():
    try:
        x, y = pyautogui.locateCenterOnScreen('retired.png')
        pyautogui.click(x, y)
        print('have players retired')
        return True
    except pyautogui.ImageNotFoundException:
        return False  


def check_preseason():
    try:
        x, y = pyautogui.locateCenterOnScreen('preseason.png')
        pyautogui.click(x, y)
        print('it is preseason')
        return True
    except pyautogui.ImageNotFoundException:
        return False  


def check_inseason():
    try:
        x, y = pyautogui.locateCenterOnScreen('inseason.png')
        pyautogui.click(x, y)
        print('it is in season')        
        return True
    except pyautogui.ImageNotFoundException:
        return False


def check_next_match():
    try:
        x, y = pyautogui.locateCenterOnScreen('tonextmatch.png')
        pyautogui.click(x, y)
        print('cursor is in to_next_match')
        return True
    except pyautogui.ImageNotFoundException:
        return False  


def check_ingame():
    try:
        pydirectinput.press('b') # pause game
        x, y = pyautogui.locateCenterOnScreen('match.png')
        pyautogui.click(x, y)
        print('it is in the match')
        return True
    except pyautogui.ImageNotFoundException:
        return False   
    

def check_training():
    try:
        x, y = pyautogui.locateCenterOnScreen('totraining.png')
        pyautogui.click(x, y)
        print('cursor is in training')
        return True
    except pyautogui.ImageNotFoundException:
        return False


def job():
    global off_flag
    global cup_flag
    if check_ingame(): # if it is in game, then end game
        end_game()
        print('waiting for end game screen')
        pyautogui.sleep(10) # game take a little bit long time to terminate
    elif check_cup(): # check if it is cup, then update score
        cup_flag = True
        pydirectinput.press('n')
        pyautogui.sleep(0.15)
    elif check_negotiations(): # in the half of the season
        if off_flag:
            print('stop program')
            exit()
        else:
            move_next_match()
        pyautogui.sleep(0.15)
    elif check_retired(): # if have players retired, screenshot
        pyautogui.hotkey('win', 'prntscrn')
        pyautogui.sleep(2)
        pydirectinput.press('n')
        pyautogui.sleep(0.15)
    elif check_preseason(): # if it is preseason, cancel and proceed
        pydirectinput.press('k')
        pydirectinput.press('n')
        pyautogui.sleep(0.15)
    elif check_offseason(): # if it is offseason, need to stop program
        if off_flag:
            print('stop program')
            exit()
        else:
            if check_training():
                print('press N to go training')
                pydirectinput.press('n')
                pydirectinput.press('n')
                pydirectinput.press('n')
                pyautogui.sleep(0.2)
                pydirectinput.press('k')
                pyautogui.sleep(0.2)
                pydirectinput.press('a')
                pydirectinput.press('a')
                pydirectinput.press('a')
                pydirectinput.press('a')
                pyautogui.sleep(0.2)
                pydirectinput.press('n')               
            else:
                print('press D to move to training')
                pydirectinput.press('d')
        pyautogui.sleep(0.15)
    elif check_inseason(): # if it is in season, go to next match
        off_flag = True
        move_next_match()           
        pyautogui.sleep(0.15)
    else: # press N to proceed in other screens
        print('press N to proceed to next stage')
        pydirectinput.press('n')
        pyautogui.sleep(0.15)


def move_next_match():
    if check_next_match():
        print('press N to proceed to next stage')
        pydirectinput.press('n')
    else:
        print('press A to move to cursor')
        pydirectinput.press('a')              


def end_game():
    try:
        x, y = pyautogui.locateCenterOnScreen('matchover.png')
        pyautogui.click(x, y)
        global cup_flag
        if cup_flag:
            x, y = pyautogui.locateCenterOnScreen('updatescore.png')
            pyautogui.click(x, y)
            print('update score for cup')
            cup_flag = False            
        with pyautogui.hold('alt'):
            pyautogui.press('tab')
        pyautogui.sleep(0.1)
        pydirectinput.press('b') # resume game
    except pyautogui.ImageNotFoundException:
        print('Error! cheat tool not open')
        exit()       


if __name__ =="__main__":
    while (True):
        job()