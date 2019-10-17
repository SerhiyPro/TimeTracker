"""
This module is used for linux-based systems
"""
import subprocess
import re
from app.osAbstract import Os


class Linux(Os):
    def get_active_window(self):
        """
        :return: the current working window
        """
        stdout, stderr = subprocess.Popen(['xprop', '-root', '_NET_ACTIVE_WINDOW'],
                                          stdout=subprocess.PIPE).communicate()
        active_window_info = re.search(b'^_NET_ACTIVE_WINDOW.* ([\\w]+)$', stdout)
        if active_window_info is None:
            return

        window_id = active_window_info.group(1)
        stdout, stderr = subprocess.Popen(['xprop', '-id', window_id, 'WM_NAME'], stdout=subprocess.PIPE).communicate()
        active_window = re.match(b"WM_NAME\\(\\w+\\) = (?P<name>.+)$", stdout)
        if not active_window:
            return

        full_window_name = active_window.group("name").strip(b'"')
        full_window_name = full_window_name.decode('utf-8') if (type(full_window_name) is bytes) else \
            str(full_window_name)
        if not full_window_name:
            return
        return full_window_name.split(" - ")

    def get_active_window_title(self):
        """
        :return: the title of current active window
        """
        return self.get_active_window()[-1]

    def get_browser_url(self):
        """
        :return: the representation of current url
        """
        browsers_tab_full_info = self.get_active_window()
        if not browsers_tab_full_info:
            return

        browsers_tab_full_info.pop()
        if not browsers_tab_full_info:
            return
        return 'Web browser: ' + "/".join(browsers_tab_full_info[::-1])

