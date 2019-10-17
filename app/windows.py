"""
This module is used for windows systems
"""
import win32gui
import uiautomation as auto
from app.osAbstract import Os


class Windows(Os):
    def get_active_window(self):
        """
        :return: the current working window
        """
        return win32gui.GetForegroundWindow()

    def get_active_window_title(self):
        """
        :return: the title of current active window
        """
        current_window = self.get_active_window()
        return win32gui.GetWindowText(current_window)

    def get_browser_url(self):
        """
        :return: the representation of current url
        """
        current_window = self.get_active_window()
        browser_control = auto.ControlFromHandle(current_window)
        edit = browser_control.EditControl()
        return 'Web browser: ' + "/" + edit.GetValuePattern().Value

