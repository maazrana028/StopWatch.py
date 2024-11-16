# StopWatch.py
I have created a simple project that imitates as a stopwatch with various options to choose from, these are start, stop, reset and exit. which the user is prompted to enter.
his Python code implements a simple stopwatch program using the time, sys, and select modules. Here's a breakdown of the code:

1. Importing Modules:

import time: This line imports the time module, which provides functions for working with time, such as getting the current time and calculating time differences.
import sys: This line imports the sys module, which provides access to system-specific parameters and functions, including stdin (standard input).
import select: This line imports the select module, which allows you to monitor multiple input/output (I/O) objects, such as file descriptors and sockets, for readiness.
2. Stopwatch Class:

The Stopwatch class represents the stopwatch functionality.
__init__(self): The constructor initializes the stopwatch object.
self.startTime = None: Stores the time when the stopwatch is started.
self.elapsedTime = 0: Stores the total elapsed time.
self.isRunning = False: Indicates whether the stopwatch is currently running.
startWatch(self): Starts the stopwatch.
If the stopwatch is not already running, it sets self.startTime to the current time and sets self.isRunning to True.
stopWatch(self): Stops the stopwatch.
If the stopwatch is running, it calculates the elapsed time by subtracting self.startTime from the current time and stores it in self.elapsedTime. It then sets self.isRunning to False.
resetWatch(self): Resets the stopwatch.
It sets self.elapsedTime to 0 and self.isRunning to False.
logWatchTime(self): Prints the total elapsed time.
It calculates the total time by adding self.elapsedTime to the time elapsed since the last startWatch call if the stopwatch is currently running.
3. Main Program:

stopwatch = Stopwatch(): Creates an instance of the Stopwatch class.
Main Loop:
The program enters a loop that continuously prompts the user for commands.
It reads the user's input using input().
Based on the command entered:
start: Calls stopwatch.startWatch().
stop: Calls stopwatch.stopWatch().
reset: Calls stopwatch.resetWatch().
exit: Breaks out of the loop, ending the program.
Monitoring Input:
After the main loop, the program enters another loop that runs as long as the stopwatch is running (stopwatch.isRunning).
This loop uses select.select() to check if there is any input available on sys.stdin (standard input).
If there is input, the loop breaks, allowing the program to proceed.
Logging Time:
Finally, the program calls stopwatch.logWatchTime() to print the total elapsed time.
time.sleep(0.0001) adds a small delay to allow the program to respond to any input before exiting.
Key Concepts:

Time Measurement: The time module is used to measure the time elapsed between events.
Input Handling: The select module allows the program to monitor input from the user without blocking.
Object-Oriented Programming: The Stopwatch class encapsulates the stopwatch functionality, making the code more organized and reusable.
This code provides a simple example of how to create a stopwatch program in Python. You can extend this code to add more features, such as displaying the time in different formats or saving the results to a file.
