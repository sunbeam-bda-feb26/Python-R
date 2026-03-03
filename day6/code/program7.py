# file handling
# - operations
#   - write contents
#   - read contents
#   - append contents
# - open()
#   - used to open a file
#   - accepts 2 parameter
#     - file name or path
#     - mode: w ('write'), a ('append'), r ('read')
# - close()
#   - close a file 
#   - if file contents are modified, without close(), the contents wont get 
#     flushed/saved on the disk
# - seek()
#   - used to change the reading/writing index
# - tell()
#   - used get the current value of reading index
# - write()
#   - used to write the contents to the file
# - read()
#   - read all the contents from a file
# - read(n)
#   - read n bytes/characters from a file
# - mode = w
#   - if a file is not present, a new empty file gets created automatically 
#   - if new contents are written, existing contents will be removed

def function1():
    # open a file
    file = open("my_file.txt", 'w')

    # write contents to the file
    file.write("India is my country. All indians are my brothers and sisters.")

    # close the file
    file.close()

    print("file contents are written")

# function1()

def function2():
    # open a file
    file = open("my_file.txt", 'a')

    # write contents to the file
    file.write("I love python programming")

    # close the file
    file.close()

    print("file contents are written")

# function2()

def function3():
    # open the file
    file = open("my_file.txt", "r")

    # read all the contents from the file
    data = file.read()
    print(f"data = {data}")

    # close the file
    file.close()

# function3()

def function4():
    # open the file
    # file reading index is set to 0
    file = open("my_file.txt", "r")

    # read 10 characters from the file
    # reading index will be updated to 10
    data = file.read(10)
    print(f"data = {data}")

    # read next 10 characters from the file
    # reading index will be updated to 20
    data = file.read(10)
    print(f"data = {data}")

    # read next 10 characters from the file
    # reading index will be updated to 30
    data = file.read(10)
    print(f"data = {data}")
    
    # close the file
    file.close()

# function4()

def function5():
    # open the file
    # reading index will set to 0
    file = open("my_file.txt", "r")

    # find the reading index position
    print(f"reading index position = {file.tell()}")

    # set the reading index to 21
    file.seek(21)

    # find the reading index position
    print(f"reading index position = {file.tell()}")
    
    # read 10 characters from the file
    data = file.read(10)
    print(f"data = {data}")

    # close the file
    file.close()

# function5()


def function6():
    # using with block
    with open("my_file.txt", "r") as file:
            
        # read all the contents from the file
        data = file.read()
        print(f"data = {data}")

        # closing file is NOT required as the with block
        # automatically closes the file/resource 
        # file.close()

function6()