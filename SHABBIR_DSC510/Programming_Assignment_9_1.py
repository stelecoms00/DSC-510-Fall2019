"""
File: Programming_Assignment_9_1.py
Name: Syed Shabbir
Date: 10/27/2019
Course: Introduction to Programming
Assignment#: 9.1

Purpose of the Program

Desc: Modify Gettysburg processing program from week 8 in order to generate a text file
      from the output rather than printing to the screen. Your program should have a new function
      called process_file which prints to the file
      (this method should almost be the same as the pretty_print function from last week.
      Keep in mind that we have print statements in main as well.
      Your program must modify the print statements from main as well.

Usage: Create a new function called process_file. This function will perform the same operations as pretty_print from week 8
       however it will print to a file instead of to the screen.
       Modify your main method to print the length of the dictionary to the file as opposed to the screen.
       This will require that you open the file twice. Once in main and once in process_file.
       Prompt the user for the filename they wish to use to generate the report.
       Use the filename specified by the user to write the file.
       This will require you to pass the file as an additional parameter to your new process_file function.

"""

import string          # library to help with removing punctuation

word_count = dict()    # creating a dictionary

def add_word(word, word_count):    # Creating an add_word function and add word into dictionary
    # use get() and provide a default value of zero when the word is not yet in the dictionary and then increment by one
    word_count[word] = word_count.get(word, 0) + 1

def process_line(line, word_count): # Creating a process_line fucntion to strip various characters/spaces and split out the words
    line = line.rstrip() # remove extra spaces
    line = line.translate(line.maketrans('', '', string.punctuation)) # remove punctuations
    line = line.lower() # convert all lines into lower case
    words = line.split() # split each line into words
    for word in words: # create loop to add each word into dictionary
        add_word(word, word_count) # calling add_word function

def pretty_print(word_count): # Creating a pretty_print fucntion
    first_line = 'Length of the dictionary: {0}'.format(len(word_count))     # Display first line of output of the program
    print(first_line)
    print('\nWord' + 'Count'.rjust(len(first_line) - 5) + '\n' + '_' * len(first_line)) # Show column headers
    for key, value in sorted(word_count.items(), key=lambda item: item[1], reverse=True): # Form a loop to display output in descending order
        line_print = ('{0}' + '{1}'.rjust(len(first_line) - len(key) - 2)).format(key, value)
        print(line_print)

def process_file(word_count, rowlen): # Creating a function process_file to generate text file from the output
    fn = fname
    with open(fn, "a") as f:
        f.write('\nWord' + 'Count'.rjust(rowlen - 5) + '\n' + '_' * rowlen + '\n') # column headers and making a line
        for key, value in sorted(word_count.items(), key=lambda item: item[1], reverse=True):
            line_print = ('{0}' + '{1}\n'.rjust(rowlen - len(key) - 2)).format(key, value) # Loop to word count output in descending order
            f.write(line_print)
    return fn

def returnFileName(): # Ask user to enter filename
    while True:
        inputname = input("Enter the filename to write to without file extension? ")
        if len(inputname) == 0:
            print("Please try again...")
            continue
        break
    global fname
    fname = inputname + ".txt"
    return fname

# Declare main function and use a main function as the main program
def main():
    returnFileName() # calling a returnFileName fucntion
    word_count = {} # Dictionary for words
    gba_file = open('gettysburg.txt', 'r') # Opening gettysburg.txt file
    for line in gba_file: # Prepare a loop to call process_line function
        process_line(line, word_count)
    first_line = 'Length of the dictionary: {0}\n'.format(len(word_count))
    fn = fname
    with open(fn, "w") as f:
        f.write(first_line)
    process_file(word_count, len(first_line)) # print out dictionary that shows frequencies of words from file
    print("The file \"{0}\" has been saved in your current folder.".format(fn)) # Prompting user that file has been saved

if __name__ == "__main__": # Execute all of the code
    main() # calling a main function

# End of Program
