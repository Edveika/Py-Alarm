import os
import vlc
import threading
import clock
import gui


def main():
    clock0 = clock.Clock()
    ui = gui.GUI(clock0)

    t1 = threading.Thread(target=run_clock, args=(clock0,))
    t2 = threading.Thread(target=ui.draw_main_window)

    t1.start()
    t2.start()
    

def run_clock(clock):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    alarm_sound_path = os.path.join(script_dir, "..", "Assets", "alarm_sound.mp3")
    alarm_sound = vlc.MediaPlayer("file://" + alarm_sound_path)

    while True:
        if clock.check_alarms() == True:
            alarm_sound.play()

main()