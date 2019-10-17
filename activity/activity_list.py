import json
from dateutil import parser

from activity.activity_single import Activity
from activity.timeentry import TimeEntry


class ActivityList:
    def __init__(self, activities=None):
        if activities is None:
            activities = []
        self.activities = activities
        self.time_entries = []

    def initialize_me(self):
        with open('activities.json', 'r') as f:
            data = json.load(f)
            activity_list = ActivityList(
                activities=self.get_activities_from_json(data)
            )
        return activity_list

    def get_activities_from_json(self, data):
        return_list = []
        for activity in data['activities']:
            return_list.append(
                Activity(
                    name=activity['name'],
                    time_entries=self.get_time_entries_from_json(activity),
                )
            )
        self.activities = return_list
        return return_list

    def get_time_entries_from_json(self, data):
        return_list = []
        for entry in data['time_entries']:
            return_list.append(
                TimeEntry(
                    start_time=parser.parse(entry['start_time']),
                    end_time=parser.parse(entry['end_time']),
                    days=entry['days'],
                    hours=entry['hours'],
                    minutes=entry['minutes'],
                    seconds=entry['seconds'],
                )
            )
        self.time_entries = return_list
        return return_list

    def serialize(self):
        return {
            'activities': self.activities_to_json()
        }

    def activities_to_json(self):
        activities_ = []
        for activity in self.activities:
            activities_.append(activity.serialize())

        return activities_

