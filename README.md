# PyAlarm

This is my first python application, without the hello world ones :) For my first python applicaiton i deciced to make an alarm clock. It uses ```tkinter``` for the graphical user interface and also has multi threading so that the GUI doesnt freeze when alarm manager is doing its thing.

![Screenshot from 2023-10-02 19-02-31](https://github.com/Edveika/Py-Alarm/assets/113787144/549804c4-7f34-4245-ad3b-bf4619706693)

# Features
1. Alarm name
2. Alarm time
3. Play a sound when alarm goes off
4. Messagebox to stop the alarm when it goes off. I could not make a separate window for this(or couldnt figure out how) due to tkinter not supporting multi threading
5. Alarm settings - you can change the settings of the alarm by double clicking an alarm in the alarm list
6. Graphical user interface(GUI)
7. Multithreading - one thread for the GUI, other for the alarm manager

# Dependencies

1. ```Tkinter```
2. ```VLC```

# Problem

Tkinter framework doesnt support threading and its documentation is not great(I had to use stackoverflow and chatgpt a lot to do basic things), I feel like it limits what I can do with it... I was going to add way more functionality but not having the ability to use multi threading really makes it difficult and inconvenient...

# License

This project is licensed under the GPL v2 [LICENSE](LICENSE).
