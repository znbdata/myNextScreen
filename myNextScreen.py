import time
import winsound
import win32api
import win32con

cursor_pos = win32api.GetCursorPos()
last_display_index = -1

def play_enter_sound():
    # Play the enter sound using the winsound module
    winsound.PlaySound("enter_sound_CC.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def play_exit_sound():
    # Play the exit sound using the winsound module
    winsound.PlaySound("exit_sound_CC.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

while True:
    new_cursor_pos = win32api.GetCursorPos()

    # Check if the mouse cursor has moved to an adjacent display
    displays = []
    num_displays = win32api.GetSystemMetrics(win32con.SM_CMONITORS)
    for i in range(num_displays):
        display = {}
        display["left"] = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN) + win32api.GetSystemMetrics(win32con.SM_CXSCREEN) * i
        display["top"] = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
        display["right"] = display["left"] + win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
        display["bottom"] = display["top"] + win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
        displays.append(display)

    display_index = -1
    for i in range(num_displays):
        if new_cursor_pos[0] >= displays[i]["left"] and new_cursor_pos[0] < displays[i]["right"]:
            display_index = i
            break

    if display_index != last_display_index:
        if display_index > last_display_index:
            play_enter_sound()
        else:
            play_exit_sound()
        last_display_index = display_index

    cursor_pos = new_cursor_pos
    time.sleep(0.1) # Sleep for 0.1 seconds to reduce CPU usage
