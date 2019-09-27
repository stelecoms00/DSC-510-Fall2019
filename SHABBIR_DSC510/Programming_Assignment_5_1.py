"""
File: Programming_Assignment_5_1.py
Name: Syed Shabbir
Date: 09/26/2019
Course: Introduction to Programming
Assignment#: 5.1

Purpose of the Program

Desc:  This program will perform various calculations (addition, subtraction, multiplication, division,
       and average calculation)
       This program will contain a variety of loops and functions.
       The program will add, subtract, multiply, divide two numbers and provide the average of multiple numbers
       input by the user.

Usage:  Define a function named performCalculation which takes one parameter.
        The parameter will be the operation being performed (+, -, *, /).
        This function will perform the given prompt the user for two numbers
        then perform the expected operation depending on the parameter that's passed into the function.
        This function will print the calculated value for the end user.
        Define a function named calculateAverage which takes no parameters.
        This function will ask the user how many numbers they wish to input.
        This function will use the number of times to run the program within a for loop
        in order to calculate the total and average.
        This function will print the calculated average.
        This program will have a main section which contains a while loop.
        The while loop will be used to allow the user to run the program until they enter a value which ends the loop.
        The main program should prompt the user for the operation they wish to perform.
        The main program should evaluate the entered data using if statements.
        The main program should call the necessary function to perform the calculation.

"""

# Welcome the user to the program
print('Welcome to my program! This program will contain Loops and Functions to perform Arithmetic Operations\n')

prg_times = int(input('How many times do you want to run this program? '))
prg_times = prg_times + 1
i = 1
while i < prg_times:
    # List of Arithmetic Operators
    oper_list = ['+', '-', '*', '/']

    # Input from user which operation to perform
    user_input = str(input('\nEnter the calculation that you want to perform (+, -, *, /): '))

    # for Loops to check the user input with the elements in list for arithmetic operations
    for x in oper_list:
        if user_input == x:
            break
        else:
            continue
    else:
        print("Try again!")
        continue

    # function to perform the calculation
    def performcalculation(oper):
        #input of two numbers from user
        num1 = float(input('Enter the first number?'))
        num2 = float(input('Enter the second number?'))
        # if conditions on each arithmetic operation
        if oper == '+':
            result = num1 + num2
        elif oper == '-':
            result = num1 - num2
        elif oper == '*':
            result = num1 * num2
        elif oper == '/':
            result = num1 / num2
        # print the calculation of two numbers
        print("The calculation of two numbers is {}".format(result))

    # Calling a function to perform calculation
    performcalculation(user_input)

    # Defining a function calculateAverage to calculate total and average
    def calculateaverage():
        print('Perform sum and average of Numbers')
        while True:
            try:
                # input the numbers from user
                nums = int(input('How many numbers you want to enter?  \n'))
                if nums == 0:
                    print('Enter a Number greater than Zero: \n')
                    continue
                break
            except:
                print('Not a valid number. Try again! \n')
        numb_add = 0

        # for loop to check where total numbers input = nums
        for i in range(0, nums):
            # Enter numbers one after another
            num_input = int(input('Enter a Number: '))
            # Calculate the sum
            numb_add = numb_add + num_input

        # Calculate the average
        average = numb_add / nums
        print("Sum of the numbers =", numb_add)
        print("Average of the numbers =", round(average, 2))

    # Calling the function calculateAverage()
    calculateaverage()
    i = i + 1