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

main()