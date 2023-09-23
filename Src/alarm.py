import os
import vlc
import alarm_data
import datetime

class Alarm:
    def __init__(self):
        self.alarms = []
        # load existing data from a file

    def mainloop():
        return 0

    def add_alarm(self, alarm):
        self.alarms.append(alarm)
    
    def remove_alarm(self, alarm):
        self.alarms.remove(alarm)

    def alarm_active(self, alarm):
        now_hours = datetime.datetime.now().hour
        now_minutes = datetime.datetime.now().minute

        if alarm.hour == now_hours and alarm.minute == now_minutes:
            return True

        return False
    
    def get_active_alarms(self):
        return 0
    
    def alarms_to_file(self):
        return 0
    
    def alarms_from_file(self):
        return 0
    
    def load_alarm_sound(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        alarm_sound_path = os.path.join(script_dir, "..", "Assets", "alarm_sound.mp3")
        self.alarm_sound = vlc.MediaPlayer("file://" + alarm_sound_path)
