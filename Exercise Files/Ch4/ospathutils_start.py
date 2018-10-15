#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  print(os.name)
  # Check for item existence and type
  print("item exist "+str(path.exists("textfile.txt")))
  print("item is file "+str(path.isfile("textfile.txt")))
  print("item is directory "+str(path.isdir("textfile.txt")))
  print("item real path"+str(path.realpath("textfile.txt")))
  print("item path and name"+str(path.split(path.realpath("textfile.txt"))))
  # Work with file paths


  # Get the modification time
  t=time.ctime(path.getmtime("textfile.txt"))
  print(t)
  print(datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))

  # Calculate how long ago the item was modified
  td=datetime.datetime.now()- datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
  print(td.seconds)

if (__name__ == "__main__"):
  main()
