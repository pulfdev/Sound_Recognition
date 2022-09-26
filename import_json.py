import json
  
# Opening JSON file
f = open('user_dictionaries.json', 'r')
  
dictionaries = json.load(f)

user_made_sounds = dictionaries["user_made_sounds"]
hotkey_dict = dictionaries["hotkey_dict"]
keyboard_dict = dictionaries["keyboard_dict"]
general_settings = dictionaries["general_settings"]
mouse_dict = dictionaries["mouse_dict"]
mode_dict = dictionaries["mode_dict"]
settings_dict = dictionaries["settings_dict"]
emergency_detection_dict = dictionaries["emergency_detection_dict"]
f.close()

def save_user_changes(dictionaries = dictionaries):
    f = open('user_dictionaries.json', 'w')
    json.dump(dictionaries, f)
    f.close()

def reset_to_default():
    f = open('default_user_dictionaries.json', 'r')
    dictionaries = json.load(f)
    f.close()
    save_user_changes(dictionaries)

def print_current_shortcuts(dictionary):
    for i in dictionary:
        if dictionary[i] != "none":
            print(i + ": " + dictionary[i])
    

