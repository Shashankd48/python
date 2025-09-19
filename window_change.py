import pyautogui
import pygetwindow as gw
import win32gui
import win32con
import time
import random
import string

def random_text(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def bring_to_front(hwnd):
    """Force a window to foreground using win32"""
    try:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # restore if minimized
        win32gui.SetForegroundWindow(hwnd)              # bring to front
        return True
    except Exception as e:
        print(f"[ERROR] Could not bring window to front: {e}")
        return False

def cycle_windows():
    windows = [w for w in gw.getAllTitles() if w.strip()]
    if not windows:
        return

    current = gw.getActiveWindow()
    try:
        idx = windows.index(current.title)
        next_title = windows[(idx + 1) % len(windows)]
    except Exception:
        next_title = windows[0]

    try:
        win = gw.getWindowsWithTitle(next_title)[0]
        if bring_to_front(win._hWnd):
            print(f"[INFO] Switched to: {next_title}")
    except Exception as e:
        print(f"[ERROR] Could not switch: {e}")

def write_in_notepad():
    try:
        win = gw.getWindowsWithTitle("Notepad")[0]
        if bring_to_front(win._hWnd):
            time.sleep(0.5)
            text = random_text()
            pyautogui.typewrite(text + "\n")
            print(f"[INFO] Wrote in Notepad: {text}")
    except IndexError:
        print("[WARN] Notepad is not open!")

def main():
    tab_interval = 30
    write_interval = 60
    last_tab = time.time()
    last_write = time.time()

    print("Script started. Press Ctrl+C to stop.")

    while True:
        now = time.time()

        if now - last_tab >= tab_interval:
            cycle_windows()
            last_tab = now

        if now - last_write >= write_interval:
            write_in_notepad()
            last_write = now

        time.sleep(1)

if __name__ == "__main__":
    main()
