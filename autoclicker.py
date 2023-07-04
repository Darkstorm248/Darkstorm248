import pyautogui
import keyboard

# Clicks per second
cps = 10

# Initialize clicker state
clicker_on = False

# Define a function to toggle the clicker state
def toggle_clicker():
    global clicker_on
    clicker_on = not clicker_on
    if clicker_on:
        print('Auto-clicker started.')
    else:
        print('Auto-clicker stopped.')

# Add a listener for the start/stop button
keyboard.add_hotkey('`', toggle_clicker)

# Add a listener for the exit button
def exit_program():
    print('Program exited.')
    keyboard.remove_all_hotkeys()
    quit()

keyboard.add_hotkey('q', exit_program)

# Loop until program is stopped
while True:
    # Check if the clicker is turned on
    if clicker_on:
        # Click the mouse
        pyautogui.click()
        # Sleep for the appropriate amount of time to achieve desired cps
        pyautogui.PAUSE = 1 / cps
        
    # Sleep for a short time to reduce CPU usage
    pyautogui.PAUSE = 0.01
