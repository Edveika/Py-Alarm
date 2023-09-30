
class AlarmData:
    def __init__(self, name, hour, minute, snooze_timer):
        self.name = name
        self.hour = hour
        self.minute = minute
        self.snooze = snooze_timer

    def get_name(self):
        return self.name
    
    def get_hour(self):
        return self.hour
    
    def get_minute(self):
        return self.minute
    
    def get_snooze(self):
        return self.snooze
    
    def set_name(self, name):
        self.name = name

    def set_hour(self, hour):
        self.hour = hour

    def set_minute(self, minute):
        self.minute = minute

    def set_snooze(self, snooze):
        self.snooze = snooze