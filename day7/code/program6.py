# functions
# - dir(): used to find the accessible members of a module

# import the os module
import os

# find the members of os module
# print(dir(os))

# find the platform on which this program is being executed
# posix = linux/macOS, 
# win32 = windows
print(f"operating system    = {os.name}")

# create a directory
# os.mkdir("my_directory")

# remove a file
# os.unlink("/tmp/my_file.txt")

# get all the environment variables
# print(os.environ)

# get a required environemnt variable
# print(f"AWS_ACCESS_KEY_ID   = {os.getenv('AWS_ACCESS_KEY_ID')}")
