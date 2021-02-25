# PushUpClock
 A simple script to encourage you to get off your arse and do some exercise regularly. Little and often is the way to go.

## What it does
When the program executes, it displays a fullscreen window that blocks interaction with any other programs for a set amount of time.

During this time you cannot exit or switch to another program. 

If you're looking for a way to pass this time, you could do some push ups, sit ups, stand up and look around, whatever you fancy.

Once the timer hits 0, you will be asked if you did the prompted exercise and reps. You can adjust the values if you did a different exercise, or different reps. Feel free to change the exercises included in the script. 

Your efforts will be saved to a CSV file in the same directory as this script, so your pathway to swole is recorded.

![Demo](https://github.com/not-matt/PushUpClock/blob/master/demo.gif)

## Requirements
- Python with Tkinter. Default Python installation includes Tkinter.
- A scheduler to run the python script. eg. Crontab, Windows Task Scheduler.


## "I hate push ups" "It's too hard"
You can adjust the script! Prompt yourself to do any exercise you want. Open "PushUpClock.py" and edit the exercises, it's very straightforward.


## Usage       
Set this script to run as often as you want using your program scheduler. I have it set to run every hour while I'm logged on using Windows Task Scheduler


## Todo
- SHOW PROGRESS,     after exercise, give option to display exercise data using matplotlib
- REPS SCALING,      give a "too hard" or "too easy" option to adjust the number of reps to do next time.

