import time
import json
import datetime
import sys

from app.osAbstract import Os
from activity import ActivityList, TimeEntry, Activity


class OsFactory:
    browsers = ('Google Chrome', 'Mozilla Firefox')

    def __init__(self):
        self.active_window_name = ""
        self.activity_name = ""
        self.start_time = datetime.datetime.now()
        self.active_list = ActivityList()
        self.initialize_active_list()
        self.os = self.get_os_instance()
        self.first_run = True

    def initialize_active_list(self):
        try:
            self.active_list.initialize_me()
        except FileNotFoundError:
            print('Json file not provided')

    @staticmethod
    def get_os_instance():
        os = Os()
        if sys.platform in ['Windows', 'win32', 'cygwin']:
            from app.windows import Windows
            os = Windows()
        elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
            from app.macos import MacOs
            os = MacOs()
        elif sys.platform in ['linux', 'linux2']:
            from app.linux import Linux
            os = Linux()
        return os

    def add_activity(self):
        end_time = datetime.datetime.now()
        time_entry = TimeEntry(self.start_time, end_time, 0, 0, 0, 0)
        time_entry.get_specific_times()

        exists = False
        for activity in self.active_list.activities:
            if activity.name == self.activity_name:
                exists = True
                activity.time_entries.append(time_entry)

        if not exists and self.active_window_name:
            activity = Activity(''.join(self.active_window_name), [time_entry])
            self.active_list.activities.append(activity)
        with open('activities.json', 'w') as json_file:
            json.dump(self.active_list.serialize(), json_file, indent=4, sort_keys=True)
            self.start_time = datetime.datetime.now()

    def run(self):
        while True:
            new_window_name = self.os.get_active_window()
            if new_window_name and any(browser in new_window_name for browser in self.browsers):
                new_window_name = self.os.get_browser_url()

            if self.active_window_name != new_window_name:
                print(''.join(self.active_window_name) if type(self.active_window_name) is list else
                      self.active_window_name)  # to see the opened window
                self.activity_name = self.active_window_name

                if not self.first_run:
                    self.add_activity()

                self.first_run = False
                self.active_window_name = new_window_name

            time.sleep(1)

