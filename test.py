from AppKit import NSWorkspace, NSApplicationActivateIgnoringOtherApps


def main():
    #safari_list = [x for x in NSWorkspace.sharedWorkspace().runningApplications() if
    #               x.bundleIdentifier() == 'com.apple.Safari']
    #safari = safari_list[0]
    #safari.activateWithOptions_(NSApplicationActivateIgnoringOtherApps)

    name = [apps["NSApplicationName"] for apps in NSWorkspace.sharedWorkspace().launchedApplications()]
    print(name)


if __name__ == '__main__':
    main()
