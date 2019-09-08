"""
File: Programming_Assignment_3_1.py
Name: Syed Shabbir
Date: 09/07/2019
Course: Introduction to Programming
Assignment#: 3.1

Purpose of the Program

Desc: Display a welcome message for your program.
      Get the company name from the user.
      Get the number of feet of fiber optic cable to be installed from the user.
      Evaluate the total cost based upon the number of feet requested.
      Display the calculated information including the number of feet requested and company name.

Usage: Your program will calculate the cost of fiber optic cable installation by multiplying the number of feet
       needed by $0.87. We will also evaluate a bulk discount.
       You will prompt the user for the number of fiber optic cable they need installed.
       Using the default value of $0.87 calculate the total expense.
       If the user purchases more than 100 feet they are charged $0.80 per foot.
       If the user purchases more than 250 feet they will be charged $0.70 per foot.
       If they purchase more than 500 feet, they will be charged $0.50 per foot.

"""

# Display a welcome message for your program
print('Welcome to the Fiber Optic Calculator!')
print('This program will calculate the Discount depending on the length of Fiber cable\n')

# Get the company name from the user
company_name = input('Enter your Company Name? ')

# Get the number of feet of fiber optic cable to be installed from the user.
fiber_length = float(input('Enter the Fiber Optic Cable Length in Feet? '))

# Conditional statements for bulk discount
if 0 <= fiber_length < 100:
    total_cost = fiber_length * 0.87
    print('The total fiber installation cost for, ' + company_name + ' is $' + str(total_cost))
elif 100 <= fiber_length < 250:
    total_cost = fiber_length * 0.80
    print(company_name + ' will get a bulk discount of $0.80 per feet, the total cost is $' + str(total_cost))
elif 250 <= fiber_length < 500:
    total_cost = fiber_length * 0.70
    print(company_name + ' will get a bulk discount of $0.70 per feet, the total cost is $' + str(total_cost))
elif fiber_length >= 500:
    total_cost = fiber_length * 0.50
    print(company_name + ' will get a bulk discount of $0.50 per feet, the total cost is $' + str(total_cost))
else:
    print('Not a valid entry')

# End of Program

