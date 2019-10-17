"""
This module is used for macOS systems
"""
from AppKit import NSWorkspace
from Foundation import NSAppleScript
from app.osAbstract import Os


class MacOs(Os):
    def get_active_window(self):
        """
        :return: the current working window
        """
        return NSWorkspace.sharedWorkspace().activeApplication()

    def get_active_window_title(self):
        """
        :return: the title of current active window
        """
        current_window = self.get_active_window()
        return current_window['NSApplicationName']

    def get_browser_url(self):
        """
        :return: the representation of current url
        """
        text_of_my_script = """tell app "google chrome" to get the url of the active tab of window 1"""
        s = NSAppleScript.initWithSource_(
            NSAppleScript.alloc(), text_of_my_script)
        results, err = s.executeAndReturnError_(None)
        return 'Web browser: ' + "/" + results.stringValue()

