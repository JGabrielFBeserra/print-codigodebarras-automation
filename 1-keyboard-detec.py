import keyboard 

def on_click():
    print("PRINTOU")
    
keyboard.add_hotkey('ctrl+alt+[', on_click)

keyboard.wait()