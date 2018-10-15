#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
  # make a duplicate of an existing file
  if path.exists("textfile.txt"):
    # get the path to the file in the current directory
    src= path.realpath("textfile.txt")
    dest = src+".bak"
    
    # let's make a backup copy by appending "bak" to the name
    shutil.copy(src,dest)
    
    # copy over the permissions, modification times, and other info
    shutil.copystat(src,dest)

    # rename the original file
    #os.rename("textfile.txt","newfile.txt")
    
    # now put things into a ZIP archive
    #rootdir, tail = path.split(src)
    #shutil.make_archive("archive","zip",rootdir)

    # more fine-grained control over ZIP files
    with ZipFile("textzip.zip","w") as newzip:
      newzip.write("textfile.txt")
      newzip.write("textfile.txt.bak")
      
if __name__ == "__main__":
  main()
