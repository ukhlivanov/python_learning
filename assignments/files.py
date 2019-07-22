# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content (overwrites existing files)
# "r" - Read - will read any existing content
# "r+" - reading and writing
# "w+" - writing and reading(overwrites existing files or creates new file)


# Basic Practice:

# http://codingbat.com/python

# More Mathematical (and Harder) Practice:

# https://projecteuler.net/archives

# List of Practice Problems:

# http://www.codeabbey.com/index/task_list

# A SubReddit Devoted to Daily Practice Problems:

# https://www.reddit.com/r/dailyprogrammer

# A very tricky website with very few hints and touch problems (Not for beginners but still interesting)

# http://www.pythonchallenge.com/



# f = open("test.txt", "a")
# f.write("line 1 line 1 \n")
# f.write("line 2 line 2 \n")
# f.write("line 3 line 3 \n")
# f.close()

# f = open("test.txt", "r")

# print(f.read())
# f.seek(0)

# a = f.readlines()
# print(f.tell())
# f.seek(0)
# b = f.readline()
# print(a)
# print(b)
# f.seek(0)
# print(f.tell())

# f.close()

# f1 = open("/home/sergey/dataset.json")
# print(f1.read())
# f1.close()




with open('test.txt', mode= 'w') as my_source:
    contents=my_source.write('line 1\nline 2\nline 3')\


with open('test.txt') as my_source:
    # contents1=my_source.readlines() #array of strings
    contents2=my_source.read() #string
    # print(contents1)
    print(contents2)