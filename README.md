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


## Installation
 1. Download this repository
![Screenshot 2021-12-11 172140](https://user-images.githubusercontent.com/32398028/145711250-f6661bd6-7345-423b-afef-9bd353e3f32d.png)

 2. Extract to `%UserProfile%`
![Screenshot 2021-12-12 113612](https://user-images.githubusercontent.com/32398028/145711300-7dbdcf5c-524e-47b3-a90a-003cde2d4b9d.png)

 3. Open Task Scheduler `Start -> "Task Scheduler"`, and click `Import Task`. In the bar, go to `%UserProfile%\PushUpClock-master` and choose `PushUpClock.xml`. Feel free to make changes to the task. It's set to run every hour once you've logged on.
![Screenshot 2021-12-12 115134](https://user-images.githubusercontent.com/32398028/145711351-fbbf884f-6382-4997-a06d-1ee2acec8a31.png)

 4. Run the task to test it was imported properly
![Screenshot 2021-12-12 115255](https://user-images.githubusercontent.com/32398028/145711401-b3042e40-83dd-4cdd-b986-73f311221467.png)

 5. PushUpClock is now active! Stick at it! 

## Todo
- SHOW PROGRESS,     after exercise, give option to display exercise data using matplotlib
- REPS SCALING,      give a "too hard" or "too easy" option to adjust the number of reps to do next time.

