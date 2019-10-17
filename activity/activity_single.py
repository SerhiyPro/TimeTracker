class Activity:
    def __init__(self, name, time_entries):
        self.name = name
        self.time_entries = time_entries

    def serialize(self):
        return {
            'name': self.name,
            'time_entries': self.make_time_entries_to_json()
        }

    def make_time_entries_to_json(self):
        time_list = []
        for time in self.time_entries:
            time_list.append(time.serialize())
        return time_list

