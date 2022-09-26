from vowel_recognition import *
from import_json import *
import pyautogui

def keyboard_mode():
    print("Keyboard mode started.")
    print_current_shortcuts(keyboard_dict)
    print("Say sounds to trigger a keyboard press.")
    mode_on = True
    while mode_on:
        sound_string = get_user_sounds(user_made_sounds) 
        print(sound_string)
        shortcut = trigger_shortcut(sound_string, keyboard_dict) 
        if shortcut == "finishkeyboardmode":
            mode_on = False
        else:
            shortcut = trigger_shortcut(sound_string, keyboard_dict)  
            if shortcut != 0:
                pyautogui.press(shortcut)
                print(shortcut) 
            
    print("Keyboard mode off.")
