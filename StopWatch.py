import time
import sys
import select

class Stopwatch:
  def __init__(self):
    self.startTime = None
    self.elapsedTime = 0
    self.isRunning = False

  def startWatch(self):
    if not self.isRunning:
      self.startTime = time.time()
      self.isRunning = True
      print("\n          Stopwatch has started.....          ")

  def stopWatch(self):
    if self.isRunning:
      self.elapsedTime = time.time() - self.startTime
      self.isRunning = False
      print("\n          Stopwatch has stopped!!!!         ")

  def resetWatch(self):
    self.elapsedTime = 0
    self.isRunning = False
    print("\n          Stopwatch has been reset :)          ")

  def logWatchTime(self):
    totalTime = self.elapsedTime
    if self.isRunning:
      totalTime += time.time() - self.startTime
    print(f"Time: {totalTime:.4f} seconds")


stopwatch = Stopwatch()

while True:
  command = input("\n\nPlease enter one of the following commands...\n>start\n>stop\n>reset\n>exit\n\n>>  ")
  if(command == "start"):
    stopwatch.startWatch()
  elif(command == "stop"):
    stopwatch.stopWatch()
  elif(command == "reset"):
    stopwatch.resetWatch()
  elif(command == "exit"):
    break


while stopwatch.isRunning:
     if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
         break
stopwatch.logWatchTime()
time.sleep(0.0001)