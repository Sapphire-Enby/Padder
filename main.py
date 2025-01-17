
import launchpad_py as launchpad
import time

# Initialize the Launchpad
lp = launchpad.Launchpad()

if lp.Open():
    print("Launchpad opened successfully!")
else:
    print("Failed to open Launchpad!")
    exit()
lp.ButtonFlush() 
lp.Reset()  # Reset the Launchpad to clear any lights
try: # when butten pressed button_press[0] should be the pad num
    print("Press buttons on the Launchpad to see their coordinates (Ctrl+C to exit).")
    while True:
        # Poll for a button press
        button_press = lp.ButtonStateRaw()
        if button_press:  # If a button press is detected
            button, state = button_press[0], button_press[1]
            print(f"Button pressed: {button}, State: {'Pressed' if state else 'Released'}")
        time.sleep(0.01)  # Slight delay to avoid CPU overload

except KeyboardInterrupt:
    print("\nExiting...")
lp.Reset()  # Reset the Launchpad before exiting
lp.Close()  # Close the connection
