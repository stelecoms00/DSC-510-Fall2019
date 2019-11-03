"""
File: Programming_Assignment_8_1.py
Name: Syed Shabbir
Date: 10/20/2019
Course: Introduction to Programming
Assignment#: 8.1

Purpose of the Program

Desc: create a program which performs three essential operations.
      It will process this .txt file: Gettysburg.txt.
      Calculate the total words, and output the number of occurrences of each word in the file.

Usage: Open the file and process each line.
       Either add each word to the dictionary with a frequency of 1 or update the word’s count by 1.
       Nicely print the output, in this case from high to low frequency.

       add_word: Add each word to the dictionary. Parameters are the word and a dictionary. No return value.

       Process_line: There is some work to be done to process the line: strip off various characters,
       split out the words, and so on. Parameters are a line and the dictionary.
       It calls the function add word with each processed word. No return value.

       Pretty_print: Because formatted printing can be messy and often particular to each situation
       (meaning that we might need to modify it later), we separated out the printing function.
       The parameter is a dictionary. No return value.

       main: We will use a main function as the main program. As usual, it will open the file
       and call process_line on each line. When finished, it will call pretty_print to print the dictionary.
       In the main function, you will need to open the file.

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
    fn = "output.txt" # the output text file name
    with open(fn, "a") as f:
        f.write('\nWord' + 'Count'.rjust(rowlen - 5) + '\n' + '_' * rowlen + '\n') # column headers and making a line
        for key, value in sorted(word_count.items(), key=lambda item: item[1], reverse=True):
            line_print = ('{0}' + '{1}\n'.rjust(rowlen - len(key) - 2)).format(key, value) # Loop to word count output in descending order
            f.write(line_print)

# Declare main function and use a main function as the main program
def main():
    word_count = {} # Dictionary for words
    gba_file = open('gettysburg.txt', 'r') # Opening gettysburg.txt file
    for line in gba_file: # Prepare a loop to call process_line function
        process_line(line, word_count)
    first_line = 'Length of the dictionary: {0}\n'.format(len(word_count))
    fn = 'output.txt'
    with open(fn, "w") as f:
        f.write(first_line)
    process_file(word_count, len(first_line)) # print out dictionary that shows frequencies of words from file
    print("The file \"{0}\" has been saved in your current folder.".format(fn)) # Prompting user that file has been saved

if __name__ == "__main__": # Execute all of the code
    main() # calling a main function

# End of Program
