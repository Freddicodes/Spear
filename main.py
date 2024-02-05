from pynput import keyboard
from AppKit import NSWorkspace, NSRunningApplication, NSApplicationActivateIgnoringOtherApps

key_to_app = {
    'a': 'com.apple.Safari',
    'b': 'com.apple.TextEdit',
}

active_keys = set()


def on_press(key):
    active_keys.add(key)


def on_release(key):
    try:
        if isinstance(key, keyboard.KeyCode) and key.char in key_to_app:
            print(f"key: {key.char}")
            app_bundle_id = key_to_app[key.char]
            # running_apps = NSWorkspace.sharedWorkspace().runningApplications()
            # app: NSRunningApplication = [x for x in running_apps if x.bundleIdentifier() == app_bundle_id]
            app = NSRunningApplication.runningApplicationsWithBundleIdentifier_(app_bundle_id)
            if app:
                app[0].activateWithOptions_(NSApplicationActivateIgnoringOtherApps)
        elif isinstance(key, keyboard.Key):
            print(f"key: {key.name}")
    except AttributeError as error:
        print(f"error: {error}")
    finally:
        if key in active_keys:
            active_keys.remove(key)


def main():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    main()
