"""
This module is used for windows systems
"""
import win32gui
import uiautomation as auto
from app.os_abstract import Os


class Windows(Os):
    def get_active_window(self):
        """
        :return: the current working window
        """
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())

    def get_browsers_tab(self):
        """
        :return: the representation of current url
        """
        current_window = self.get_active_window()
        web_page_info = current_window.split('-')[0]
        return f'Web browser: {web_page_info}'

