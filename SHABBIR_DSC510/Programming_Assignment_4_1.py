"""
File: Programming_Assignment_4_1.py
Name: Syed Shabbir
Date: 09/19/2019
Course: Introduction to Programming
Assignment#: 4.1

Purpose of the Program

Desc: Display a welcome message for your program.
      Get the company name from the user.
      Get the number of feet of fiber optic cable to be installed from the user.
      A function with two parameters
      A call to the function (feet and cost)
      The application should calculate the cost based upon the number of feet being ordered
      A printed message displaying the company name and the total calculated cost

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
feet = float(input('Enter the Fiber Optic Cable Length in Feet? '))

# Defining a function for Cost Calculation with 2 parameters
def costcal(feet, cost):
    price = feet * cost
    return float(price)


# Cost will vary with no. of feet being installed
if feet >= 500:
    cost = 0.5
elif 250 <= feet < 500:
    cost = 0.7
elif 100 <= feet < 250:
    cost = 0.8
elif 0 <= feet < 100:
    cost = 0.87
else:
    print('Not a valid entry')

# Calling function
total_cost = costcal(feet, cost)

# Print the total cost of fiber
print('The total calculated cost of fiber for ' + company_name + ' is $' + str(total_cost))

# End of Program




