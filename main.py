
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
def getButton():
    lp.ButtonFlush() 
    while True:
        # Poll for a button press
        button_press = lp.ButtonStateRaw()
        if button_press:  # If a button press is detected
            button, state = button_press[0], button_press[1]
            print(f"Button pressed: {button}, State: {'Pressed' if state else 'Released'}")
            return button
        time.sleep(0.01)  # Slight delay to avoid CPU overload
def getColor():
    return (3,3)
def updatePad(button,colorTuple):
    lp.LedCtrlRaw(button,colorTuple[0],colorTuple[1])
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
