#########################################################
#Author : Kyle Stranick                                 #
#Class : ITN160                                         #
#Class Section : 401                                    #
#Date : 9/19/2023                                       #
#Assignment:Assignment 4-Commission calculation program #
#Version : 3.02                                         #
#########################################################

###################
#Syntax References:
###################
#Cannon, Jason. (2016). Python Succinctly., Syncfusion Inc.
#Gupta, Anubhav. Slither into Python. (2021?)
#https://www.tutorialspoint.com/python/python_if_else.htm
#https://www.tutorialspoint.com/python/python_functions.htm
#https://www.w3schools.com/python/
#https://www.pluralsight.com  I have a subscription
################
# Version Notes:
################
#Version 1.01: implementation of [if not] to negate any inputs that are not (A,B,C) [cont.]
#Version 1.01: implementation of return to end program with invalid inputs
#Version 1.02: implementation of if amount < 10000 to negate any value less than 10000
#Version 2.01: designated variables for output sentence to shorten length for code [pos] and [cos]
#Version 2.02: implementation of while True loop and try/except blocks to loop program when wrong inout is entered
#Version 2.02: implementation quit input with break to close program
#Version 2.02: implementation of continue to loop until desired input is achieved
#Version 2.03: set variable percentage equal to 0 due to reference error
#Version 3.01: implementation of def function [parameter] to make code reusable and easier to read
#Version 3.01: use of return function to return the value when called if true
#Version 3.01: established variables percentage and commission with implementation of def function
#Version 3.01: originally had 2 try/except blocks but removed the outer due to redundancy
#Version 3.02: added inner while True loop on amount block to loop when wrong values are input
#Version 3.02: removed percentage = 0 I assumed I did not need anymore please correct if wrong**
# defining function to implement into the program for reuse across program
def finding_percentage(product, amount):
    if product == 'A':
        if 10000 <= amount <= 19999:
            return 5
        elif 20000 <= amount <= 39999:
            return 7.5
        elif amount >= 40000:
            return 9  # Each return will provide the percentage when if true
    elif product == 'B':
        if 10000 <= amount <= 19999:
            return 6
        elif 20000 <= amount <= 39999:
            return 8
        elif amount >= 40000:
            return 10
    elif product == 'C':
        if 10000 <= amount <= 19999:
            return 3
        elif 20000 <= amount <= 39999:
            return 4.5
        elif amount >= 40000:
            return 5.5


def calculate_commission(percentage, amount):
    return (percentage * 0.01) * amount


def main():
    print('\nWelcome to the Sale Commission Calculation Program')
    # assigned variables to output string to cut length of sentence
    pos = 'The percentage of the sale was'  # pos means percentage of sale
    cos = 'the amount of the commission was'  # cos means commission of sale

    while True:
        # product = input().upper() allows for both uppercase and lower case input
        product = input('\nWhat product was sold?\t(A,B,C)  or Q to quit: ').upper()
        if product == 'Q':
            print('\nGoodbye!')
            break

        if product not in ['A', 'B', 'C', 'Q']:
            print('Invalid option, please select A, B, C, or Q.')
            continue

        while True:  # Will loop this input section until correct value is entered
            try:
                amount = float(input('\nWhat was the sales amount?: '))
                if amount < 10000:
                    print('Invalid amount. Please enter an amount of 10,000 or more.')
                    continue
                break
            except ValueError:
                print('Enter valid number for sales amount.')
        percentage = finding_percentage(product, amount)
        commission = calculate_commission(percentage, amount)
        print(f'\n{pos} {percentage}% and {cos} ${commission:.2f}.')


if __name__ == '__main__':
    main()
