"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
import os  # first you need to import the module 'os'

# set the cwd to 'chapter10'
# os.chdir('chapter10')

# now 'file_reader.py' and 'pi_digits.txt' are both in the cwd
contents = open(r'C:\Users\iulia\Desktop\CS_1\Intro-Python-I\src\foo.txt')
text = contents.read()
print(text)
contents.close()

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
# import os.path
# path = 'C:/Users/iulia/Desktop/CS_1/Intro-Python-I/src/'



# name_of_file = raw_input("bar")

# new_file = os.path.join(path, name_of_file+".txt")         

added_new_file = open('bar.txt', "w")

in_file = """
So weary with disasters, tugg’d with fortune,
That I would set my life on any chance,
To mend, or be rid on’t.
"""

added_new_file.write(in_file)

added_new_file.close()