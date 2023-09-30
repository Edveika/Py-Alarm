import threading
import alarm
import gui

def main():
    # Creation of objects
    alarms = alarm.Alarm()
    ui = gui.GUI(alarms)

    # Creates 2 threads:
    # 1st - for the user interface(the main thread, as TK is not threading-safe)
    # 2nd - for alarm loop using threading
    alarm_thread = threading.Thread(target=alarms.mainloop)

    # Starts both of those threads
    alarm_thread.start()
    ui.draw()

    # If ui if closed we can safely stop the alarm logic
    alarms.set_exit_flag()

main()