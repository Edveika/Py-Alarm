
class Alarm:
    def __init__(self, name, hour, minute):
        self.name = name
        self.hour = hour
        self.minute = minute

    def get_name(self):
        return self.name
    
    def get_hour(self):
        return self.hour
    
    def get_minute(self):
        return self.minute
    
    def set_name(self, name):
        self.name = name

    def set_hour(self, hour):
        self.hour = hour

    def set_minute(self, minute):
        self.minute = minute