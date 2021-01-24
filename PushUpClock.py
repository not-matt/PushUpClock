import tkinter as tk
import tkinter.font as tkFont
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox
import datetime
import random
import csv
import sys
import os

"""
██████╗ ██╗   ██╗███████╗██╗  ██╗██╗   ██╗██████╗      ██████╗██╗      ██████╗  ██████╗██╗  ██╗
██╔══██╗██║   ██║██╔════╝██║  ██║██║   ██║██╔══██╗    ██╔════╝██║     ██╔═══██╗██╔════╝██║ ██╔╝
██████╔╝██║   ██║███████╗███████║██║   ██║██████╔╝    ██║     ██║     ██║   ██║██║     █████╔╝ 
██╔═══╝ ██║   ██║╚════██║██╔══██║██║   ██║██╔═══╝     ██║     ██║     ██║   ██║██║     ██╔═██╗ 
██║     ╚██████╔╝███████║██║  ██║╚██████╔╝██║         ╚██████╗███████╗╚██████╔╝╚██████╗██║  ██╗
╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝          ╚═════╝╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝

A simple script to encourage you to get off your arse and do some exercise regularly. Little and often is the way to go.



USAGE:        Set this script to run as often as you want using Windows task manager. I have it set to run every hour while I'm logged on.

WHAT IT DOES: When the program executes, it displays a fullscreen window that blocks interaction with any other programs for a set amount of time.
              During this time you cannot exit or switch to another program. 
              If you're looking for a way to pass this time, you could do some push ups, sit ups, stand up and look around, whatever you fancy.
              Once the timer hits 0, you will be asked if you did the prompted exercise and reps. You can adjust the values if you did a different exercise, or different reps. Feel free to change the exercises below.
              Your efforts will be saved to a CSV file in the same directory as this script, so your pathway to swole is recorded.

TODO:         SHOW PROGRESS,     after exercise, give option to display exercise data using matplotlib
              REPS SCALING,      give a "too hard" or "too easy" option to adjust the number of reps to do next time.
"""



###########################
# SETTINGS 
#
EXERCISES = {"Push ups": 10,                             # Exercise will be randomly chosen from these options
             "Clean and Press": 8,                       # Format: {exercise: reps}
             "Sit ups": 20,   
             "Goblet Squats": 20}
HOLD_TIME = 15                                           # Number of seconds for exercise countdown. Switching to other programs, or exiting this program will be blocked during this time.
HOLD_MESSAGE = f"Drop and give me =REPS= =EXERCISE=!"    # Message displayed during countdown to get you off your ass. =REPS= and =EXERCISE= will be replaced appropriately
LOG_FILE = "log.csv"                                     # Name of log file. Must be in same directory as this program. Will be created if it doesnt exist.
ACTIVE_HOURS = ("09:00", "21:00")                        # Active hours (format "HOUR:MINUTE"). The program will only run between these hours. 
#
###########################


class CountdownWindow(tk.Tk):
    def __init__(self, message):
        super().__init__()
        #window = tk.Tk()
        self.attributes("-topmost", True ,'-fullscreen', True)
        self.bind("<FocusOut>", self.on_focus_out)
        self.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.wm_title("Pushups")

        fontStyle = tkFont.Font(family="Lucida Grande", size=50)
        self.message_label = tk.Label(self, font=fontStyle, text=message)
        self.message_label.pack(fill=tk.BOTH, expand=True, anchor="center")

        fontStyle = tkFont.Font(family="Lucida Grande", size=30)
        self.message_label = tk.Label(self, font=fontStyle, text="Computer locked for...")
        self.message_label.pack(fill=tk.BOTH, expand=True, anchor="center")

        fontStyle = tkFont.Font(family="Lucida Grande", size=500)
        self.countdown_label = tk.Label(self, font=fontStyle)
        self.countdown_label.pack(fill=tk.BOTH, expand=True, anchor="center")

        # call countdown first time 
        self.allowed_to_close = False   
        self.countdown(HOLD_TIME)
        # root.after(0, countdown, 5)
        self.mainloop()

    def countdown(self, count):
        # change text in label        
        self.countdown_label['text'] = count
        if count > 0:
            # call countdown again after 1000ms (1s)
            self.after(1000, self.countdown, count-1)
        elif count == 0:
            self.allowed_to_close = True
            self.on_exit()

    def on_focus_out(self, val):
        self.focus_force()

    def on_exit(self):
        if self.allowed_to_close:
            self.destroy()

class GetRepsWindow(tk.Tk):
    def __init__(self, exercise, reps):
        super().__init__()
        self.wm_title("Record your effort")

        positionRight = int(self.winfo_screenwidth()/2 - 140)
        positionDown = int(self.winfo_screenheight()/2 - 90)
        self.geometry("+{}+{}".format(positionRight, positionDown))
        self.resizable(0, 0)

        self.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.bind('<Return>', self.get_number)

        self.reps = tk.IntVar(value=reps)
        self.exercise = tk.StringVar(value=exercise)
        # self.showprogress = tk.IntVar(value=0)

        self.formframe = tk.Frame(padx=10, pady=10)
        self.buttonframe = tk.Frame(padx=5, pady=5)

        self.repslabel = tk.Label(self.formframe, text="How many reps did you do?")
        self.repsinput = tk.Spinbox(self.formframe, from_=0, to=1000, textvariable=self.reps)
        self.exerciselabel = tk.Label(self.formframe, text="What exercise did you do?")
        self.exerciseinput = tk.OptionMenu(self.formframe, self.exercise, *EXERCISES.keys())
        # self.showprogressinput = tk.Checkbutton(self.buttonframe, text='Show my progress', variable=self.showprogress)
        self.cancelbutton = tk.Button(self.buttonframe, text="I didn't do it", command=self.on_exit, width=10)
        self.okbutton = tk.Button(self.buttonframe, text="I did it", command=self.get_number, width=10)

        # self.exerciseinput.current(0) 
        self.repslabel.grid(column=0, row=0, sticky="E")
        self.repsinput.grid(column=1, row=0, sticky="NSEW")
        self.exerciselabel.grid(column=0, row=1, sticky="E")
        self.exerciseinput.grid(column=1, row=1, sticky="NSEW")
        # self.showprogressinput.pack(side="left", padx=5)
        self.okbutton.pack(side="right", padx=5)
        self.cancelbutton.pack(side="right", padx=5)
        

        self.formframe.pack(fill="both")
        self.buttonframe.pack(fill="x")

        self.focus_force()
        self.attributes("-topmost", True)
        self.mainloop()

    def on_exit(self):
        self.reps.set(0)
        self.destroy()

    def get_number(self, event=None):
        if self.repsinput.get():
            try:
                int(self.repsinput.get())
                self.reps.set(self.repsinput.get())
                self.destroy()
            except ValueError:
                messagebox.showwarning("Illegal Value", "Not an integer.\nPlease try again.")
        else:
            messagebox.showwarning("Illegal Value", "Not an integer.\nPlease try again.")

def displayExerciseData(log_file_path):
    with open(log_file_path, "r", newline="") as log_file:
        log_reader = csv.reader(log_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in log_reader:
            print(row)

def main():
    # Only run if between active hours
    start_hour = datetime.datetime.strptime(ACTIVE_HOURS[0], "%H:%M").time()
    end_hour = datetime.datetime.strptime(ACTIVE_HOURS[1], "%H:%M").time()
    time_now = datetime.datetime.now().time()

    if not start_hour < time_now < end_hour:
        return 0

    exercise, reps = random.choice(list(EXERCISES.items()))
    message = HOLD_MESSAGE.replace("=REPS=", str(reps)).replace("=EXERCISE=", exercise)

    # run countdown window
    cw = CountdownWindow(message)

    # get reps and exercise from user
    getreps = GetRepsWindow(exercise, reps)
    reps = getreps.reps.get()
    exercise = getreps.exercise.get()
    # showprogress = getreps.showprogress.get()

    # save data to log file
    if reps:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        log_file_path = os.path.join(dir_path, LOG_FILE)
        with open(log_file_path, "a", newline="") as log_file:
            log_writer = csv.writer(log_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            now = datetime.datetime.now()
            date_time = now.strftime("%m/%d/%Y %H:%M:%S")
            log_writer.writerow([date_time, exercise, reps])

    # # If the user asked, then display the saved data
    # if showprogress:
    #     displayExerciseData(log_file_path)



if __name__ == "__main__":
    sys.exit(main())



# rw = record_window()
# root = tk.Tk() # create main window
# #root.iconify() # minimize main window 
# root.withdraw() # hide main window 
# print(reps)