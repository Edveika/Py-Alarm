import tkinter
import alarm
import alarm_data
from tkinter import messagebox

class GUI:
    def __init__(self, clock):
        self.clock = clock
        self.alarm_names = []

    def draw(self):
        window = tkinter.Tk()
        window.geometry("400x600")
        window.title("PyAlarm")

        def on_double_click(event):
            selected_index = self.alarm_listbox.curselection()
            if selected_index:
                self.alarm_settings_window(selected_index[0])

        self.alarm_listbox = tkinter.Listbox(window, selectmode=tkinter.SINGLE, height=10)
        self.alarm_listbox.pack(padx=10, pady=10, fill=tkinter.BOTH, expand=True)

        self.add_alarm_button = tkinter.Button(window, text="Add Alarm", command=self.new_alarm_window)
        self.add_alarm_button.pack(padx=10, pady=10, side=tkinter.BOTTOM, anchor=tkinter.CENTER)
 
        self.alarm_listbox.bind("<Double-Button-1>", on_double_click)

        tkinter.mainloop()

    def new_alarm_window(self):
        window = tkinter.Tk()
        window.title("New Alarm")

        def set_selected_values():
            selected_name = alarm_name_entry.get()
            selected_hours = hours_spinbox.get()
            selected_minutes = minutes_spinbox.get()
            selected_snooze = snooze_spinbox.get()
            
            new_alarm = alarm_data.AlarmData(str(selected_name), int(selected_hours), int(selected_minutes), int(selected_snooze))

            if self.clock.alarm_exists(new_alarm):
                messagebox.showerror("Error", "Alarm with this time already exists.")
                window.destroy()
            else:
                self.clock.add_alarm(new_alarm)
                self.alarm_listbox.insert(tkinter.END, selected_name)
                self.alarm_names.append(selected_name)
                window.destroy()

        # Name of the alarm
        current_alarm_name = "Alarm name"
        alarm_name_entry = tkinter.Entry(window)
        alarm_name_entry.insert(0, current_alarm_name)
        alarm_name_entry.pack()

        # Hours
        hours_frame = tkinter.Frame(window)
        hours_frame.pack()
        hours_label = tkinter.Label(hours_frame, text="Hours:")
        hours_label.pack(side="left")
        hours_spinbox = tkinter.Spinbox(hours_frame, from_=0, to=23)
        hours_spinbox.pack(side="left")

        # Minutes
        minutes_frame = tkinter.Frame(window)
        minutes_frame.pack()
        minutes_label = tkinter.Label(minutes_frame, text="Minutes:")
        minutes_label.pack(side="left")
        minutes_spinbox = tkinter.Spinbox(minutes_frame, from_=0, to=59)
        minutes_spinbox.pack(side="left")

        # Snooze Timer
        snooze_frame = tkinter.Frame(window)
        snooze_frame.pack()
        snooze_label = tkinter.Label(snooze_frame, text="Snooze Timer (minutes):")
        snooze_label.pack(side="left")
        snooze_spinbox = tkinter.Spinbox(snooze_frame, from_=0, to=60)
        snooze_spinbox.pack(side="left")

        # Set button that creates a new alarm
        get_values_button = tkinter.Button(window, text="Set Selected Values", command=set_selected_values)
        get_values_button.pack()

    def active_alarm_window(self, alarm):
        window = tkinter.Tk()
        window.title("Alarm")

        def stop_alarm():
            print("Alarm Stopped")

        def snooze_alarm():
            print("Alarm Snoozed")

        alarm_time_label = tkinter.Label(window, text="08:00", font=("Helvetica", 36))
        alarm_time_label.pack()

        alarm_name_label = tkinter.Label(window, text="Morning Alarm", font=("Helvetica", 18))
        alarm_name_label.pack()

        stop_button = tkinter.Button(window, text="Stop Alarm", command=stop_alarm, bg="red", fg="white", font=("Helvetica", 14))
        stop_button.pack()

        snooze_button = tkinter.Button(window, text="Snooze", command=snooze_alarm, bg="blue", fg="white", font=("Helvetica", 14))
        snooze_button.pack()

    def alarm_settings_window(self, alarm_index):
        window = tkinter.Tk()
        window.geometry("300x250")
        window.title("Alarm Settings")
        alarm = self.clock.get_alarms()[alarm_index]

        def refresh_listbox():
            # Refreshes the listbox of the main menu
            self.alarm_listbox.delete(0, tkinter.END)
            for item in self.alarm_names:
                self.alarm_listbox.insert(tkinter.END, item)

        def save_changes():
            new_alarm_name = alarm_name_entry.get()
            alarm.set_name(new_alarm_name)
            self.alarm_names[alarm_index] = new_alarm_name

            new_hour = int(hour_spinbox.get())
            alarm.set_hour(new_hour)

            new_minute = int(minute_spinbox.get())
            alarm.set_minute(new_minute)

            new_snooze = int(snooze_spinbox.get())
            alarm.set_snooze(new_snooze)

            refresh_listbox()
            window.destroy()

        def delete_alarm():
            self.clock.get_alarms().pop(alarm_index)
            self.alarm_names.pop(alarm_index)
            
            refresh_listbox()
            window.destroy()

        alarm_name_label = tkinter.Label(window, text="Alarm Name:")
        alarm_name_label.pack()

        # Alarm name settings
        alarm_name_entry = tkinter.Entry(window)
        alarm_name_entry.insert(0, alarm.get_name())
        alarm_name_entry.pack()

        # Hours settings
        hour_label = tkinter.Label(window, text="Hours:")
        hour_label.pack()
        hour_spinbox = tkinter.Spinbox(window, from_=0, to=23, values=alarm.get_hour())
        hour_spinbox.pack()

        # Minutes settings
        minute_label = tkinter.Label(window, text="Minutes:")
        minute_label.pack()
        minute_spinbox = tkinter.Spinbox(window, from_=0, to=59, values=alarm.get_minute())
        minute_spinbox.pack()

        # Snooze timer settings
        snooze_label = tkinter.Label(window, text="Snooze Timer (minutes):")
        snooze_label.pack()
        snooze_spinbox = tkinter.Spinbox(window, from_=0, to=60, values=alarm.get_snooze())
        snooze_spinbox.pack()

        # Saves the changes to an already existing alarm
        save_button = tkinter.Button(window, text="Save", command=save_changes)
        save_button.pack()

        save_button = tkinter.Button(window, text="Delete alarm", command=delete_alarm)
        save_button.pack()