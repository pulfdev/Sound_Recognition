from keyboard_mode import *
from hotkey_mode import *
from mouse_mode import * 
from settings_mode import *
from emergency_detection_mode import *

def run_program():
    print("Welcome to sound recognition.")
    if user_made_sounds["is_training_complete"] == "False":
        train_default_sounds(4)
        user_made_sounds["is_training_complete"] = True
        save_user_changes()
    if emergency_detection_dict["emergency_info_up_to_date"] == "False":
        set_emergency_info()
    is_program_running = True 
    while is_program_running:
        print("Please say a mode.")
        print_current_shortcuts(mode_dict)
        mode_shortcut_sound = get_user_sounds()
        mode = trigger_shortcut(mode_shortcut_sound, mode_dict)
        if mode == "mousemode":
            mouse_mode()
        elif mode == "keyboardmode":
            keyboard_mode()
        elif mode == "hotkeymode":
            hotkey_mode()
        elif mode == "settingsmode":
            settings_mode()
        elif mode == "emergencydetectionmode":
            if emergency_detection_dict["emergency_info_up_to_date"] == "False":
                print("You cannot use emergency detection mode until you have updated your emergency info in settings.")
            else: 
                print("Welcome to emergency detection mode. To trigger an alert make the sound " + emergency_detection_dict["Emergency_string"] + " were 'l' means a long held sound and 's' means a short held sound.")  
                emergency_detection_mode() 
        elif mode == "finishprogram":
            save_user_changes()
            is_program_running = False
            print("Thank you for using Sound Recognition")
        else:
            print("Please repeat mode.") 
        
run_program() 