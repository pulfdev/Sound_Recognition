from vowel_recognition import *
from import_json import *
import pyautogui

def hotkey_mode(threshold = general_settings["threshold"]):
    print("Hotkey mode started.")
    print_current_shortcuts(hotkey_dict)
    print("Say sounds to trigger a hotkey.")
    mode_on = True
    while mode_on:
        sound_string = get_user_sounds(user_made_sounds) 
        print(sound_string)
        shortcut = trigger_shortcut(sound_string, hotkey_dict)
        if shortcut == "finishhotkeymode":
            mode_on = False
        else:
            if shortcut != 0:
                shortcut_list = shortcut.split(" , ")
                if len(shortcut_list) == 2:
                    pyautogui.hotkey(shortcut_list[0], shortcut_list[1], interval=0.25)
                elif len(shortcut_list) == 3:
                    pyautogui.hotkey(shortcut_list[0], shortcut_list[1], shortcut_list[2], interval=0.25)
                print(shortcut)
        
    print("Hotkey mode off.")



