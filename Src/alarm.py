import os
import vlc
import time
import alarm_data
import datetime

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
        # load existing alarms from a file to self.alarms

    def mainloop(self):
        while self.run == True:
            self.get_active_alarms()
        
    def get_alarms(self):
        return self.alarms

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
        for alarm in self.alarms:
            if self.alarm_active(alarm):
                self.active_alarms.append(alarm)

    def play_alarm_sound(self):
        self.alarm_sound.play()
        time.sleep(4)
        self.alarm_sound.stop()

    def set_exit_flag(self):
        self.run = False