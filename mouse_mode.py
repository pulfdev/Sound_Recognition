from volume_recognition import *
from vowel_recognition import *
import pyautogui
import os

def get_direction():
    print("Say direction")
    verified = False
    while verified == False:
        sound_string = get_user_sounds(user_made_sounds) 
        print(sound_string)
        direction = trigger_shortcut(sound_string, mouse_dict) 
        if direction == "right":
            verified = True
        elif direction == "left":
            verified = True
        elif direction == "up":
            verified = True
        elif direction == "down":
            verified = True
        elif direction == "click":
            verified = True
        elif direction == "rightclick":
            verified = True
        elif direction == "doubleclick":
            verified = True
        elif direction == "tripleclick":
            verified = True
        elif direction == "finishmousemode":
            verified = True
        else:
            print("Please repeat direction.")
    return direction

def if_loud_move(energies, threshold, direction):
    if direction == "click":
        pyautogui.click()
    elif direction == "rightclick":
        pyautogui.click(button="right")
    elif direction == "doubleclick":
        pyautogui.click(clicks=2)
    elif direction == "tripleclick":
        pyautogui.click(clicks=3)
    else:
        for i in energies:
            amount_to_move = (pow(3,(i-threshold)) - pow(3,(-threshold))) * 500 
            if i > threshold:
                if direction == "right":
                    pyautogui.move(amount_to_move, 0, 0.5)
                elif direction == "left":
                    pyautogui.move(-amount_to_move, 0, 0.5)
                elif direction == "up":
                    pyautogui.move(0, -amount_to_move, 0.5)
                elif direction == "down":
                    pyautogui.move(0, amount_to_move, 0.5)
                else:
                    return False
    return 0

def voice_to_mouse_move(direction, threshold = general_settings["threshold"]):
    start_and_save_recording()
    energies_variable = energies()
    if_loud_move(
        energies_variable, threshold, direction
    )  # TO DO: set threshold as global variable
    os.remove("recordings/pythonrecording.wav")
    return energies_variable
    

def count_silence(direction, energies_variable, threshold = general_settings["threshold"], count=0):
    # normalised_energies = energies_variable - threshold
    energies_variable[energies_variable < threshold] = 0
    if direction == "click" or direction == "doubleclick" or direction == "rightclick"or direction == "tripleclick":
        count = general_settings["length_of_silence"] + 1
    else: 
        if np.all(energies_variable == 0):
            count += 1
        else:
            count = 0
    return count

def movement_loop(direction, threshold = general_settings["threshold"]):
    count = 0
    while count < general_settings["length_of_silence"]:
        energies_variable = voice_to_mouse_move(direction, threshold)
        count = count_silence(direction, energies_variable, threshold, count)

def mouse_mode(threshold = general_settings["threshold"]):
    print("Mouse mode started.")
    print_current_shortcuts(mouse_dict)
    print("Say sounds to decide direction then make a noise until the mouse is in the correct position.")
    mouse_mode_on = True
    while mouse_mode_on == True:
        direction = get_direction()
        if direction == "finishmousemode":
            mouse_mode_on = False
            print("Mouse Mode Ended")
        else:
            print("Make sound to move mouse or wait for the click.")
            movement_loop(direction, threshold)
    print("Mouse mode off.")



