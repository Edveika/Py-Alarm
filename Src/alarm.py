import alarm_data
import datetime

class Alarm:
    def __init__(self):
        self.alarms = []

    def add_alarm(self, alarm):
        self.alarms.append(alarm)
    
    def remove_alarm(self, alarm):
        self.alarms.remove(alarm)

    def check_alarms(self):
        now_hours = datetime.datetime.now().hour
        now_minutes = datetime.datetime.now().minute

        for alarm in self.alarms:
            if alarm.hour == now_hours and alarm.minute == now_minutes:
                return True

        return False
    
    def get_active_alarm(self):
        return 0
    
