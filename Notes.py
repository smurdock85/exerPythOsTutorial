## To-DO
# * Execute code examples in separate cells.
  # * import os
  # * print(dir(os))
  #* print(os.getcwd())
  # os.chdir()
  # os.listdir()
  # os.mkdir() - make a new directory folder in the repository
  # os.makedirs() - make a new directory with a subdirectory in the repository
  # os.rmdir() - remove the new directory
  # os.removedirs() - remove the new directory with subdirectory
  # os.rename()
  # print(os.stat())
  # from datetime import datetime
  # print(datetime.fromtimestamp())
  # os.walk()
  # print(os.environ.get('HOME'))
  # os.path.join()
  # os.path.basename()
  # os.path.dirname()
  # os.path.split()
  # os.path.exists()
  # os.path.isdir()
  # os.path.isfile()
  # os.path.splitext()
  # add a comment in a cell with a url for official Python documentation (not shown in the video - Google it)
  # add a comment in a cell with a url for a tutorial on the OS module in the official documentation (not shown in the video - look through the documentation to find it)

import os

print(dir(os)) 

print(os.getcwd())

# Get current working directory
os.getcwd()

# Change directory, this requires a path to change to
os.chdir(path)

# List directory, you can pass a path, but by default it is in the current directory
os.listdir()

# Creating directories
mkdir()  # Use for making one directory
makedirs(). # Use if you want to create multiple directories at once

# Remove directories
rmdir(file). # Recommended use case
removedirs(file)  # Removes intermediate directories if specified

# Rename a file or folder
os.rename(‘test.txt’, ‘demo.txt’). # This renames text.txt to demo.txt

# Info about files
os.stat(test.txt)

for dirpath, dirnames, filenames in os.walk(routepath): 
    print(‘Current Path:’, dirpath)
    print(‘Directories:’, dirnames)
    print(‘Files:’, filenames)
    print()

# Access home directory location by grabbing home environment variable
os.environ.get(‘HOME’). # Returns a path

# To properly join two files together use os.path.join()
file_path = os.path.join(os.environ.get(‘HOME’), ‘test.txt’)

## os.path has other useful methods

os.path.basename
# This will grab filename of any path we are working on

os.path.dirname(‘/tmp/test.txt’)
# returns the directory /tmp

os.path.split(‘/tmp/test.txt’)
# returns both the directory and the file as a tuple

os.path.exists(‘/tmp/test.txt’)
# returns a boolean

os.path.isdir(‘/tmp/test.txt’)
# returns False

os.path.isfile(‘/tmp/test.txt’)
# returns True

os.path.splitext(‘/tmp/test.txt’)
# Splits file route of the path and the extension

# source doc 
# https://docs.python.org/3/ 

# Tutorial on OS
# https://docs.python.org/3/tutorial/stdlib.html 