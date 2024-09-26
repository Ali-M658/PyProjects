from pynput import keyboard
from pynput.keyboard import Controller
from pynput import mouse
from pynput.mouse import Button, Controller as mousecont
import time

keyboard_controller = Controller()

key_sequence = []
mouse_clicks = []

def on_press(key):
    try:
        key_sequence.append(key.char)
        print(f'\'{key.char}\' pressed')
    except AttributeError:
        key_sequence.append(key)
        print(f'Special key {key} pressed')
def on_release(key):
    print(f'Key {key} released')
    if key == keyboard.Key.esc:
        replay()
        return False

def replay():
    print('Replaying keys...')
    for key in key_sequence:
        if isinstance(key, keyboard.Key):
            keyboard_controller.press(key)
            keyboard_controller.release(key)
        else:
            keyboard_controller.type(key)
        time.sleep(0.2)

def press(x, y, button, pressed):
    print(f'{button} {"pressed" if pressed else "released"} at ({x},{y})')
    mouse_clicks.append((x, y, button, pressed))
    if pressed and button == Button.middle:
        mouserep()
        return False

mouse_controller = mousecont()

def mouserep():
    print('Replaying mouse inputs...')
    for x, y, button, pressed in mouse_clicks:
        mouse_controller.click(button)
        mouse_controller.position = (x, y)
        if pressed:
            mouse_controller.press(button)
        else:
            mouse_controller.release(button)
        time.sleep(0.2)


with keyboard.Listener(on_press=on_press, on_release=on_release) as keyboard_listener, \
     mouse.Listener(on_click=press) as mouse_listener:
    keyboard_listener.join()
    mouse_listener.join()