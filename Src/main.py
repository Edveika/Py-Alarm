import threading
import alarm
import gui

def main():
    # Creation of objects
    alarm_manager = alarm.AlarmManager()
    gui_manager = gui.GuiManager(alarm_manager)

    # Creates 2 threads:
    # 1st - for the user interface(the main thread, as TK is not threading-safe)
    # 2nd - for alarm loop using threading
    alarm_manager_thread = threading.Thread(target=alarm_manager.mainloop)

    # Starts both of those threads
    alarm_manager_thread.start()
    gui_manager.draw()

    # If ui if closed we can safely stop the alarm logic
    alarm_manager.set_exit_flag()

main()