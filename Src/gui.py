import tkinter
import clock
import alarm

class GUI:
    def __init__(self, clock):
        self.clock = clock

    def draw_main_window(self):
        window = tkinter.Tk()
        window.geometry("400x600")
        window.title("PyAlarm")

        self.alarm_listbox = tkinter.Listbox(window, selectmode=tkinter.SINGLE, height=10)
        self.alarm_listbox.pack(padx=10, pady=10, fill=tkinter.BOTH, expand=True)

        self.add_alarm_button = tkinter.Button(window, text="Add Alarm", command=self.draw_new_alarm_window)
        self.add_alarm_button.pack(padx=10, pady=10, side=tkinter.BOTTOM, anchor=tkinter.CENTER)

        tkinter.mainloop()

    def draw_new_alarm_window(self):
        window = tkinter.Tk()
        window.title("Alarm Settings")

        def set_selected_values():
            selected_hours = hours_spinbox.get()
            selected_minutes = minutes_spinbox.get()
            selected_snooze = snooze_spinbox.get()
            
            new_alarm = alarm.Alarm(int(selected_hours), int(selected_minutes))
            self.clock.add_alarm(new_alarm)
            window.destroy()

        # Hours
        hours_frame = tkinter.Frame(window)
        hours_frame.pack()
        hours_label = tkinter.Label(hours_frame, text="Hours:")
        hours_label.pack(side="left")
        hours_spinbox = tkinter.Spinbox(hours_frame, from_=0, to=24)
        hours_spinbox.pack(side="left")

        # Minutes
        minutes_frame = tkinter.Frame(window)
        minutes_frame.pack()
        minutes_label = tkinter.Label(minutes_frame, text="Minutes:")
        minutes_label.pack(side="left")
        minutes_spinbox = tkinter.Spinbox(minutes_frame, from_=0, to=60)
        minutes_spinbox.pack(side="left")

        # Snooze Timer
        snooze_frame = tkinter.Frame(window)
        snooze_frame.pack()
        snooze_label = tkinter.Label(snooze_frame, text="Snooze Timer (minutes):")
        snooze_label.pack(side="left")
        snooze_spinbox = tkinter.Spinbox(snooze_frame, from_=0, to=60)
        snooze_spinbox.pack(side="left")

        get_values_button = tkinter.Button(window, text="Set Selected Values", command=set_selected_values)
        get_values_button.pack()

    def draw_ongoing_alarm_window(self, ):
        return 0


