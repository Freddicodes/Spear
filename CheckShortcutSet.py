from CheckShortcutInterface import CheckShortcutInterface


class CheckShortcutSet(CheckShortcutInterface):
    def __init__(self):
        super().__init__()
        self.shortcut_set = set()
        self.valid = False

    def is_valid(self, shortcut):
        return self.valid

    def on_press(self, key):
        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
            self.valid = True
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

    def on_release(self, key):
        try:
            print('alphanumeric key {0} released'.format(
                key.char))
            self.valid = False
        except AttributeError:
            print('special key {0} released'.format(
                key))
