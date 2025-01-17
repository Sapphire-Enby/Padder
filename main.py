
import launchpad_py as launchpad
import time

# Initialize the Launchpad

lp = launchpad.Launchpad()

if lp.Open():
    print("Launchpad opened successfully!")

else:
    print("Failed to open Launchpad!")
    exit()

lp.Reset()  # Reset the Launchpad to clear any lights

PAD_CACHE = {}
COLOR_SELECTOR={0: (1, 0), 1: (2, 0), 2: (3, 0), 16: (1, 1), 17: (2, 2), 18: (3, 3), 32: (0, 1), 33: (0, 2), 34:(0, 3)}

def getButton():
    lp.ButtonFlush() 
    print("press a SQUARE button on the pad to set the color")
    while True:
        # Poll for a button press
        button_press = lp.ButtonStateRaw()
        if button_press:  # If a button press is detected
            button, state = button_press[0], button_press[1]
            print(f"Button pressed: {button}, State: {'Pressed' if state else 'Released'}")
            return button
        time.sleep(0.01)  # Slight delay to avoid CPU overload

def get_valid_input(color):
    while True:
        try:
            user_input = int(input(f"Enter a number (0-3) for {color}: "))
            if user_input in range(4):  # range(4) means 0, 1, 2, 3
                return user_input
            else:
                print("Invalid input. Please enter a number between 0 and 3.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def getColor():
    redVal = get_valid_input('red')
    greenVal = get_valid_input('green')
    return (redVal , greenVal)

def updatePad(button,colorTuple):
    PAD_CACHE[button] = colorTuple
    lp.LedCtrlRaw(button,colorTuple[0],colorTuple[1])

def save_light_config(filename="light_config.json"):
    import json
    config = {k:v for k,v in PAD_CACHE.items() if v !=(0,0)}   
    # Save to a JSON file
    with open(filename, "w") as f:
        json.dump(config, f)
    print(f"Light configuration saved to {filename}")

def map_color_select():
    lp.reset() # clear map
    for k,v in COLOR_SELECTOR.items(): #  render colors in profile (dont update cache)
        lp.LedCtrlRaw(k,v[0],v[1])
    sel=getButton()  # prompt to choose button for color selection
    color=COLOR_SELECTOR.get(sel,(0,0)) # grab color, with blank as default
    PAD_CACHE[sel]=color # update cache pad cache
    lp.reset() # clear pad
    for k,v in PAD_CACHE.items(): # render cache
        lp.LedCtrlRaw(k,v[0],v[1])
    
    

def main():
    print("select Color")
    colorTuple=getColor()
    print("selectButton")
    button = getButton()
    updatePad(button,colorTuple)
    input("waiting to exit")
    lp.Reset()
    lp.Close()

if __name__ == "__main__":
    main()
