import pyautogui
from PIL import ImageGrab
import keyboard
import time

running = True

def on_key_event(e):
    global running
    if e.event_type == keyboard.KEY_DOWN and e.name == '0':
        running = False

keyboard.hook(on_key_event)
0
while running:
    time.sleep(0.1)
    x, y = pyautogui.position()
    pixel_color = ImageGrab.grab().getpixel((x, y))
    print(f"Mouse position: X = {x}, Y = {y}")
    print(f"Pixel RGB: R = {pixel_color[0]}, G = {pixel_color[1]}, B = {pixel_color[2]}")

keyboard.unhook_all()  # Clean up the keyboard hook

