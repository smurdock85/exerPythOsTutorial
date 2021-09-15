import os

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