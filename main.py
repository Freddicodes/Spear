from pynput import keyboard
from CheckShortcutSet import CheckShortcutSet


def main():
    strategy = CheckShortcutSet()

    with keyboard.Listener(on_press=strategy.on_press, on_release=strategy.on_release) as listener:
        listener.join()


if __name__ == '__main__':
    main()
