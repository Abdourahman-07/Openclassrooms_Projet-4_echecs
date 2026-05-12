from datetime import datetime


class Round:
    def __init__(self, name, matches=None, start_datetime=None, end_datetime=None):
        self.name = name
        self.matches = matches or []
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime

    def start(self):
        self.start_datetime = datetime.now()

    def end(self):
        self.end_datetime = datetime.now()

    def add_match(self, match):
        self.matches.append(match)