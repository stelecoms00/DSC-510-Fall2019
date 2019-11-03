"""
File: Programming_Assignment_6_1.py
Name: Syed Shabbir
Date: 10/03/2019
Course: Introduction to Programming
Assignment#: 6.1

Purpose of the Program

Desc:   Create a program which contains a list of temperatures.
        Program will populate the list based upon user input.
        Program will determine the number of temperatures in the program,
        determine the largest temperature, and the smallest temperature.

Usage:  Create an empty list called temperatures.
        Allow the user to input a series of temperatures along with a sentinel value which will stop the user input.
        Evaluate the temperature list to determine the largest and smallest temperature.
        Print the largest temperature.
        Print the smallest temperature.
        Print a message tells the user how many temperatures are in the list.

"""

# Welcome the user to the program
print('Welcome to my program! This program will determine the number of temperatures, the largest temperature, and the smallest temperature\n')

# This is a function of Temperature program
def temp_prgrm():
    # This is an empty list called temperatures
    temperatures = []
    while True:      # while loop
        try:
            user_input = int(input("Enter the temperature or type 99999 to end? ")) # input of temperature from user
            if user_input != 99999: # condition to continue taking user input until user entered sentinel value 99999
                temperatures.append(user_input) # appending user temperature in the list of temperatures
                continue
            break
        except: # Make sure user enter the correct numeric value for temperature
            print("Please enter the numeric value for temperature")
    if len(temperatures) > 0: # if user entered valid temperatures and list is not empty
        print("\nThe Largest temperature is {}".format(max(temperatures))) # print largest temperature
        print("\nThe Smallest temperature is {}".format(min(temperatures))) # print smallest temperature
        print("\nThe total number of temperatures entered are {}".format(len(temperatures))) # print number of temperatures
    else: # if user entered 99999 at the very first input then program will be ended without any temperature
        print("The program is ended as user entered 99999 and has not entered any temperature")

temp_prgrm() # Calling a function

#End of Program
