# deadtunes

A relatively simple way to find unavailable songs in your iTunes library.

## Usage

1. Start iTunes
3. Fullscreen iTunes and go to songs view and scroll to the top  (make sure iCloud Download column is visible)
2. Run `deadtunes.py`
4. Position your mouse cursor in the top left corner of the iTunes window
5. Press F5
6. Position your mouse cursor in the bottom right corner of the iTunes window
7. Press F6 and then esc
8. Wait for the script to finish or hold q to quit
9. The script will output a list of songs that are unavailable in your library to `deadtunes.txt` in the same directory as the script
10. profit

## Requirements
Only works on Windows. Requires Python 3.6+ and the following modules:
- pyautogui
- pyperclip
- keyboard
- pyscreeze