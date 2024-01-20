from CheckShortcutInterface import CheckShortcutInterface


class CheckShortcutSet(CheckShortcutInterface):
    def __init__(self):
        self.shortcut_set = set()

    def is_valid(self, shortcut):
        raise NotImplementedError
