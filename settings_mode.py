from vowel_recognition import *
from import_json import *
from emergency_detection_mode import *

def change_shortcut_sounds(dictionary):
    shortcut = input("Which shortcut do you want to change the shortcut sound for?")
    if shortcut in dictionary:
        print("Say what you want the new shortcut sound to be?")
        new_shortcut_sound = get_user_sounds(user_made_sounds).strip()
        shortcut_sound_in_use = is_shortcut_sound_in_use(dictionary, new_shortcut_sound)
        
        if shortcut_sound_in_use == "not in use":
            dictionary[shortcut] = new_shortcut_sound
            save_user_changes()
        else:
            print("This shortcut sound is already being used for " + shortcut_sound_in_use + ".")
            x = input("Would you like to overwrite this? y/n?")
            if x == "y": 
                dictionary[shortcut_sound_in_use] = "none"
                dictionary[shortcut] = new_shortcut_sound
                save_user_changes()
            else:
                print("Shortcut sound for " + shortcut + " has not changed.")
    else:
        print("The shortcut you entered is not available in this mode.")

def is_shortcut_sound_in_use(dictionary, sound):
    while True:
        try:
            shortcut_sound = list(dictionary.keys())[list(dictionary.values()).index(sound)]
            print(shortcut_sound[0])
            return shortcut_sound[0]
        except ValueError:
            return "not in use"


def new_user_sound(number): 
    new_sound_name = input("Name new sound:")
    train_sounds(new_sound_name, number)

def change_a_shortcut_sound():
    print("Which mode would you like to change the shortcut for?")
    print(settings_dict["a"] + ": Keyboard mode \n" + settings_dict["b"]+ ": Mouse mode \n" + settings_dict["c"]+ ": Hotkey Mode \n" + settings_dict["d"] + ": Shortcuts for modes \n")
    sound_string = get_user_sounds(user_made_sounds) 
    print(sound_string)
    x = trigger_shortcut(sound_string, settings_dict) 
    if x == "a": 
        change_shortcut_sounds(keyboard_dict)
        print("Your changes have been implemented.")
    elif x == "b":
        change_shortcut_sounds(mouse_dict)
        print("Your changes have been implemented.")
    elif x == "c":
        change_shortcut_sounds(hotkey_dict)
        print("Your changes have been implemented.")
    elif x == "d":  
        change_shortcut_sounds(mode_dict)  
        print("Your changes have been implemented.")
    else: 
        print("Not an option. Please enter a, b, c or d.")
    

def settings_mode(user_made_sounds = user_made_sounds):
    print("Settings Mode Started.")
    mode_on = True
    while mode_on:
        print("What would you like to do? \n" + settings_dict["a"]+ ": Change a shortcut sound. \n" + settings_dict["b"]+ ": Create a custom sound \n" + settings_dict["c"]+ ": Train default sounds \n" + settings_dict["d"]+ ": Other settings. \n" + settings_dict["e"]+ ": Reset to default settings. \n"+ settings_dict["g"]+ ": Update emergency info \n" + settings_dict["f"]+ ": Leave settings")
        sound_string = get_user_sounds(user_made_sounds) 
        print(sound_string)
        x = trigger_shortcut(sound_string, settings_dict)
        if x == "a":
            change_a_shortcut_sound()
        elif x == "b":
            new_user_sound(4)
        elif x == "c": 
            print("Do you want to \n" + settings_dict["a"]+ ": train default sounds from scratch \n" + settings_dict["b"]+ ": add to the existing ")
            sound_string = get_user_sounds(user_made_sounds) 
            print(sound_string)
            y = trigger_shortcut(sound_string, settings_dict)
            if y =="a":
                user_made_sounds = {"is_tutorial_complete": "False", "": "", " ": "", "finishkeyboardmode": "finishkeyboardmode", "finishhotkeymode": "finishhotkeymode", "ah": "ah", "ay": "ay", "ee": "ee"}
                train_default_sounds(4)
            elif y == "b":    
                train_default_sounds(4)
            else:
                print("Not an option. Please enter a or b.")
            save_user_changes()
        elif x == "d":
            print("Change \n" + settings_dict["a"]+ ": Threshold (How loud the sound has to be) \n" + settings_dict["b"]+ ": Length of silence (How long the silence in mouse mode before you have to say the direction) ")
            sound_string = get_user_sounds(user_made_sounds) 
            print(sound_string)
            y = trigger_shortcut(sound_string, settings_dict)
            if y == "a":
                print("The current threshold is " + general_settings["threshold"]+".")
                z = input("What would you like the new threshold to be? Suggested: between 0.075 and 0.125. Press X to cancel.").strip()
                is_number = z.replace(".", "").isnumeric()
                if is_number:
                    general_settings["threshold"] = z
                elif z != "X" and z != "x":
                    print("Please enter a number or X if you want to cancel.")
            if y == "b":
                print("The current length of silence is " + general_settings["length_of_silence"]+".")
                z = input("What would you like the new length of silence to be? Note: must be an integer. Press X to cancel.").strip()
                is_integer = z.isnumeric()
                if is_integer:
                    general_settings["length_of_silence"] = z
                elif z != "X" and z != "x":
                    print("Please enter an integer or X if you want to cancel.")
        elif x == "e":
            print("Are you sure you want to reset to default settings? You will lose all your trained sounds. " + settings_dict["a"]+ ": Yes  " + settings_dict["b"]+ ": No")
            sound_string = get_user_sounds(user_made_sounds) 
            print(sound_string)
            y = trigger_shortcut(sound_string, settings_dict)
            if y == "a":
                reset_to_default() 
                print("System has been reset to default settings.")
            else:
                print("System has NOT been reset.") 
        elif x == "f":
            print("Exiting settings...")
            save_user_changes()
            mode_on = False
        elif x == "g":
            set_emergency_info()
        else: 
            print("Not an option. Please enter a, b, c, d, e or f.")

            



