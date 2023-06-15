import pytesseract
from PIL import Image
import pygetwindow as gw
import pyautogui

# Get the window
discord_windows = gw.getWindowsWithTitle('Discord')
if discord_windows:
    discord_window = discord_windows[0]
    # Get the window's location and size
    x, y, width, height = discord_window.left, discord_window.top, discord_window.width, discord_window.height
    # Capture the screen region corresponding to the window
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    # Use OCR to extract text
    text = pytesseract.image_to_string(screenshot)
    print(text)
else:
    print("Discord window not found")
