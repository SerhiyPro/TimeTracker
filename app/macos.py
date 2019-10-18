"""
This module is used for macOS systems
"""
from AppKit import NSWorkspace
from Foundation import NSAppleScript
from app.os_abstract import Os


class MacOs(Os):
    def get_active_window(self):
        """
        :return: the current working window
        """
        return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']

    def get_browsers_tab(self):
        """
        :return: the representation of current url
        """
        text_of_my_script = """tell app "google chrome" to get the url of the active tab of window 1"""
        s = NSAppleScript.initWithSource_(
            NSAppleScript.alloc(), text_of_my_script)
        results, err = s.executeAndReturnError_(None)
        web_page_info = results.stringValue()
        return 'Web browser: {}'.format(web_page_info)
