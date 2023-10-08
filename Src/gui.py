import tkinter
import alarm
import alarm_data
from tkinter import messagebox
import threading
import time

class GuiManager:
    def __init__(self, clock):
        self.clock = clock
        self.list_alarm_names = []
        self.run = True
        alarm_check_thread = threading.Thread(target=self.check_alarms)
        alarm_check_thread.start()

    def draw(self):
        window = tkinter.Tk()
        window.geometry("400x600")
        window.title("PyAlarm")
        
        menu_bar = tkinter.Menu(window)
        window.config(menu=menu_bar)

        file_menu = tkinter.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Alarm", menu=file_menu)

        file_menu.add_command(label="New alarm", command=self.new_alarm_window)

        def on_double_click(event):
            selected_index = self.alarm_listbox.curselection()
            if selected_index:
                self.alarm_settings_window(selected_index[0])

        self.alarm_listbox = tkinter.Listbox(window, selectmode=tkinter.SINGLE, height=10)
        self.alarm_listbox.pack(padx=10, pady=10, fill=tkinter.BOTH, expand=True)
        self.alarm_listbox.bind("<Double-Button-1>", on_double_click)

        tkinter.mainloop()

        # Close application flag
        self.run = False

    def new_alarm_window(self):
        window = tkinter.Tk()
        window.title("New Alarm")

        def set_selected_values():
            selected_name = alarm_name_entry.get()
            selected_hours = int(hours_spinbox.get())
            selected_minutes = int(minutes_spinbox.get())
            
            if selected_hours > 23 or selected_hours < 0 or selected_minutes > 59 or selected_minutes < 0:
                messagebox.showerror("Error", "Hour or minute value is out of range [0;23], [0;59]")
                window.destroy()
            else:
                new_alarm = alarm_data.Alarm(str(selected_name), selected_hours, selected_minutes)

                if self.clock.alarm_exists(new_alarm):
                    messagebox.showerror("Error", "Alarm with this time already exists.")
                    window.destroy()
                else:
                    self.clock.add_alarm(new_alarm)
                    list_alarm_name = selected_name + " " + "{:02d}".format(selected_hours) + ":" + "{:02d}".format(selected_minutes)
                    self.alarm_listbox.insert(tkinter.END, list_alarm_name)
                    self.list_alarm_names.append(list_alarm_name)
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

        # Set button that creates a new alarm
        get_values_button = tkinter.Button(window, text="Set Selected Values", command=set_selected_values)
        get_values_button.pack()

    def refresh_listbox(self):
        # Refreshes the listbox of the main menu
        self.alarm_listbox.delete(0, tkinter.END)
        for item in self.list_alarm_names:
            self.alarm_listbox.insert(tkinter.END, item)

    def alarm_settings_window(self, alarm_index):
        window = tkinter.Tk()
        window.geometry("300x250")
        window.title("Alarm Settings")
        alarm = self.clock.get_alarms()[alarm_index]

        def save_changes():
            new_hour = int(hour_spinbox.get())
            new_minute = int(minute_spinbox.get())
            if new_hour > 23 or new_hour < 0 or new_minute > 59 or new_minute < 0:
                messagebox.showerror("Error", "Hour or minute value is out of range [0;23], [0;59]")
                window.destroy()
            else:
                alarm.set_hour(new_hour)
                alarm.set_minute(new_minute)

                new_alarm_name = alarm_name_entry.get()
                list_new_alarm_name = new_alarm_name + " " + "{:02d}".format(new_hour) + ":" + "{:02d}".format(new_minute)
                alarm.set_name(new_alarm_name)
                self.list_alarm_names[alarm_index] = list_new_alarm_name

                self.refresh_listbox()
                window.destroy()

        def delete_alarm():
            self.clock.get_alarms().pop(alarm_index)
            self.list_alarm_names.pop(alarm_index)
            
            self.refresh_listbox()
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

        # Saves the changes to an already existing alarm
        save_button = tkinter.Button(window, text="Save", command=save_changes)
        save_button.pack()

        save_button = tkinter.Button(window, text="Delete alarm", command=delete_alarm)
        save_button.pack()

    def ongoing_alarm_box(self, alarm):
            result = messagebox.askquestion("Alarm: " + alarm.get_name(), "Dismiss the alarm?", icon='info', type=messagebox.OK)
            if result == "ok":
                self.clock.remove_active_alarm(alarm)
                self.list_alarm_names.remove(alarm.get_name() + " " + "{:02d}".format(int(alarm.get_hour())) + ":" + "{:02d}".format(int(alarm.get_minute())))
                self.refresh_listbox() 
    
    def check_alarms(self):
        while self.run:
            # Cool py syntax
            alarms = [alarm for alarm in self.clock.get_alarms() if self.clock.alarm_is_active(alarm)]
            for alarm in alarms:
                self.ongoing_alarm_box(alarm)
        time.sleep(1)