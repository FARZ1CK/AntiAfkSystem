import keyboard
import time

print("""'-' - Start
'+' hold - Stop
""")

first = True
def press(key, wait):
    keyboard.press(key)
    time.sleep(wait)
    keyboard.release(key)

while True:
    if keyboard.is_pressed("-"):
        first = False
    if first == False:
        press("a", 0.3)
        press ("d", 0.3)
    if keyboard.is_pressed('+'):
        first = True
