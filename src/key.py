from pynput import keyboard


def on_press(key):
    try:
        print('alphanumeric key `{0}` pressed'.format(key.char))
        listener.stop()
    except AttributeError:
        print('special key `{0}` pressed'.format(key))
        

def on_release(key):
    print('{0} released'.format(
        key))
    try :
        if key == key.esc:
            # Stop listener
            return False
    except AttributeError:
        if key.char == 'q':
            return False
    

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()