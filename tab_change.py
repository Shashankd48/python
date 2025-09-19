import pyautogui
import time
import random
import string

def random_text(length=10):
    """Generate random string of given length"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def switch_tabs():
    # Simulate Ctrl + Tab (works for browsers and some apps)
    pyautogui.hotkey("ctrl", "tab")

def write_random_text():
    text = random_text()
    pyautogui.typewrite(text + "\n")

def main():
    tab_interval = 30   # seconds
    write_interval = 60 # seconds

    last_tab = time.time()
    last_write = time.time()

    print("Script started. Press Ctrl+C to stop.")

    while True:
        now = time.time()

        # Switch tab every 30s
        if now - last_tab >= tab_interval:
            switch_tabs()
            last_tab = now
            print("[INFO] Switched tab")

        # Write text every 60s
        if now - last_write >= write_interval:
            write_random_text()
            last_write = now
            print("[INFO] Wrote random text")

        time.sleep(1)

if __name__ == "__main__":
    main()
