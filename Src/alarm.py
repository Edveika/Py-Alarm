import os
import vlc
import time
import alarm_data
import datetime
import threading

class Alarm:
    def __init__(self):
        def load_alarm_sound():
            script_dir = os.path.dirname(os.path.abspath(__file__))
            alarm_sound_path = os.path.join(script_dir, "..", "Assets", "alarm_sound.mp3")
            self.alarm_sound = vlc.MediaPlayer("file://" + alarm_sound_path)

        self.run = True
        self.alarms = []
        self.active_alarms = []
        load_alarm_sound()

    def mainloop(self):
        while self.run == True:
            self.get_ongoing_alarms()
            if len(self.active_alarms) > 0:
                self.play_alarm_sound()
            time.sleep(1)

    def get_alarms(self):
        return self.alarms

    def add_alarm(self, alarm):
        self.alarms.append(alarm)
    
    def alarm_exists(self, alarm):
        for existing_alarm in self.alarms:
            if alarm.get_hour() == existing_alarm.get_hour() and alarm.get_minute() == existing_alarm.get_minute():
                return True
        
        return False

    def remove_alarm(self, alarm):
        self.alarms.remove(alarm)

    def get_active_alarms(self):
        return self.active_alarms
    
    def add_active_alarm(self, active_alarm):
        self.active_alarms.append(active_alarm)

    def remove_active_alarm(self, active_alarm):
        self.alarms.remove(active_alarm)
        self.active_alarms.remove(active_alarm)

    def alarm_is_active(self, alarm):
        now_hours = datetime.datetime.now().hour
        now_minutes = datetime.datetime.now().minute

        if alarm.hour == now_hours and alarm.minute == now_minutes:
            return True

        return False

    def get_ongoing_alarms(self):
        for alarm in self.alarms:
            if self.alarm_is_active(alarm) and not alarm in self.active_alarms:
                self.add_active_alarm(alarm)

    def play_alarm_sound(self):
        self.alarm_sound.play()
        time.sleep(4)
        self.alarm_sound.stop()

    def set_exit_flag(self):
        self.run = False