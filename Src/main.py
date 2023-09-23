import os
import threading
import alarm
import gui

def main():
    alarms = alarm.Alarm()
    ui = gui.GUI(alarms)

    alarm_thread = threading.Thread(target=alarms.mainloop)
    ui_thread = threading.Thread(target=ui.draw)

    alarm_thread.start()
    ui_thread.start()
    
# def run_clock(clock):
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     alarm_sound_path = os.path.join(script_dir, "..", "Assets", "alarm_sound.mp3")
#     alarm_sound = vlc.MediaPlayer("file://" + alarm_sound_path)

#     while True:
#         if clock.check_alarms() == True:
#             alarm_sound.play()

main()