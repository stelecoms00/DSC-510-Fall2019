"""
File: Programming_Assignment_2_1.py
Name: Syed Shabbir
Date: 09/03/2019
Course: Introduction to Programming
Assignment#: 2.1

Purpose of the Program

Desc: Display a welcome message for your user.
      Retrieve the company name from the user.
      Retrieve the number of feet of fiber optic cable to be installed from the user.

Usage: Calculate the installation cost of fiber optic cable by multiplying the total cost as the number
       of feet times $0.87.
       Print a receipt for the user including the company name, number of feet of fiber to be installed,
       the calculated cost, and total cost in a legible format.
"""

# Take username as input and display a welcome message for your user.
user_name = input("Enter your name? ")
print("Welcome, {} to Fiber Installation Cost Calculation Program". format(user_name))

# Retrieve the company name from the user.
company_name = input("Enter your Company Name? ")

# Retrieve the fiber optic cable length from the user in feet & convert variable type from string to integer.
fiber_length = int(input("Enter the Fiber Optic Cable Length in Feet? "))

# Installation cost calculation of fiber optic cable.
total_cost = fiber_length * 0.87

# Print a receipt for the user.
print("User Receipt")
print("User Name: {}". format(user_name))
print("Company Name: {}". format(company_name))
print("Length of Fiber to be Installed: {}ft". format(fiber_length))
print("Calculated Installation per feet: $0.87")
print("Total Installation Cost: ${:,.2f}". format(total_cost))


