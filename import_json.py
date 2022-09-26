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
    

# pip install -r requirements.txt

# JSON doesnt allow comments

# // word shortcut keys  
# // Ctrl + A -- Select all contents of the page.
# // Ctrl + B -- Bold highlighted selection.
# // Ctrl + C -- Copy selected text.
# // Ctrl + X -- Cut selected text.
# // Ctrl + N -- Open new/blank document.
# // Ctrl + O -- Open options.
# // Ctrl + P -- Open the print window.
# // Ctrl + F -- Open find box.
# // Ctrl + I -- Italicise highlighted selection.
# // Ctrl + K -- Insert link.
# // Ctrl + U -- Underline highlighted selection.
# // Ctrl + V -- Paste.
# // Ctrl + Y -- Redo the last action performed.
# // Ctrl + Z -- Undo last action.
# // Ctrl + G -- Find and replace options.
# // Ctrl + H -- Find and replace options.
# // Ctrl + J -- Justify paragraph alignment.
# // Ctrl + L -- Align selected text or line to the left.
# // Ctrl + Q -- Align selected paragraph to the left.
# // Ctrl + E -- Align selected text or line to the center.
# // Ctrl + R -- Align selected text or line to the right.
# // Ctrl + M -- Indent the paragraph.
# // Ctrl + T -- Hanging indent.
# // Ctrl + D -- Font options.
# // Ctrl + Shift + F -- Change the font.
# // Ctrl + Shift + > -- Increase selected font +1.
# // Ctrl + ] -- Increase selected font +1.
# // Ctrl + [ -- Decrease selected font -1.
# // Ctrl + Shift + * -- View or hide non printing characters.
# // Ctrl + (Left arrow) -- Move one word to the left.
# // Ctrl + (Right arrow) -- Move one word to the right.
# // Ctrl + (Up arrow) -- Move to the beginning of the line or paragraph.
# // Ctrl + (Down arrow) -- Move to the end of the paragraph.
# // Ctrl + Del -- Delete word to the right of the cursor.
# // Ctrl + Backspace -- Delete word to the left of the cursor.
# // Ctrl + End -- Move cursor to end of the document.
# // Ctrl + Home -- Move cursor to the beginning of the document.
# // Ctrl + Space -- Reset highlighted text to default font.
# // Ctrl + 1 -- Single-space lines.
# // Ctrl + 2 -- Double-space lines.
# // Ctrl + 5 -- 1.5-line spacing.
# // Ctrl + Alt + 1 Change text to heading 1.
# // Ctrl + Alt + 2 Change text to heading 2.
# // Ctrl + Alt + 3 Change text to heading 3.
# // F1 -- Open help.
# // Shift + F3 -- Change case of selected text.
# // Shift + Insert -- Paste.
# // F4 -- Repeat the last action performed (Word 2000+).
# // F7 -- Spell check selected text and/or document.
# // Shift + F7 -- Activate the thesaurus.
# // F12 -- Save as.
# // Ctrl + S -- Save.
# // Shift + F12 -- Save.
# // Alt + Shift + D -- Insert the current date.
# // Alt + Shift + T -- Insert the current time.
# // Ctrl + W -- Close document.

# //excel shortcut keys 

# //F2 -- Edit the selected cell.
# // F5 -- Go to a specific cell.
# // F7 -- Spell check selected text and/or document.
# // F11 -- Create chart
# // Ctrl + Shift + ; -- Enter the current time.
# // Ctrl + ; -- Enter the current date
# // Alt + Shift + F1 -- Insert new worksheet.
# // Shift + F3 -- Open the Excel formula window.
# // Shift + F5 -- Bring up the search box
# // Ctrl + A -- Select all contents of a worksheet.
# // Ctrl + B -- Bold highlighted selection.
# // Ctrl + I -- Italicize highlighted selection.
# // Ctrl + C -- Copy selected text.
# // Ctrl + V -- Paste
# // Ctrl + D -- Fill
# // Ctrl + K -- Insert link
# // Ctrl + F -- Open find and replace options.
# // Ctrl + G -- Open go-to options.
# // Ctrl + H -- Open find and replace options.
# // Ctrl + U -- Underline highlighted selection.
# // Ctrl + Y -- Underline selected text.
# // Ctrl + 5 -- Strikethrough highlighted selection.
# // Ctrl + O -- Open options.
# // Ctrl + N -- Open new document.
# // Ctrl + P -- Open print dialog box.
# // Ctrl + S -- Save.
# // Ctrl + Z -- Undo last action.
# // Ctrl + F9 -- Minimize current window.
# // Ctrl + F10 -- Maximize currently selected window.
# // Ctrl + F6 -- Switch between open workbooks/windows.
# // Ctrl + Page up & Page Down -- Move between Excel worksheets in the same document.
# // Ctrl + Tab -- Move between two or more open Excel files
# // Alt + = -- Create the formula to sum all of the above cells.
# // Ctrl + -- Insert the value of above cell into the current cell.
# // Ctrl + Shift + ! -- Format number in comma format.
# // Ctrl + Shift + $ -- Format number in currency format.
# // Ctrl + Shift + # -- Format number in date format.
# // Ctrl + Shift + % -- Format number in percentage format.
# // Ctrl + Shift + ^ -- Format number in scientific format.
# // Ctrl + Shift + @ -- Format number in time format.
# // Ctrl + (Right arrow) -- Move to next section of text.
# // Ctrl + Space -- Select entire column.
# // Shift + Space -- Select entire row.
# // Ctrl + W -- Close document.

# //outlook shortcut keys
# // Alt + S -- Send the email.
# // Ctrl + C -- Copy selected text.
# // Ctrl + X -- Cut selected text.
# // Ctrl + P -- Open print dialog box.
# // Ctrl + K -- Complete name/email typed in address bar.
# // Ctrl + B -- Bold highlighted selection.
# // Ctrl + I -- Italicize highlighted selection.
# // Ctrl + U -- Underline highlighted selection.
# // Ctrl + R -- Reply to an email.
# // Ctrl + F -- Forward an email.
# // Ctrl + N -- Create a new email.
# // Ctrl + Shift + A -- Create a new appointment to your calendar.
# // Ctrl + Shift + O -- Open the outbox.
# // Ctrl + Shift + I -- Open the inbox.
# // Ctrl + Shift + K -- Add a new task.
# // Ctrl + Shift + C -- Create a new contact.
# // Ctrl + Shift+ J -- Create a new journal entry.