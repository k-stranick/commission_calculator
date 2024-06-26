#########################################################
#Author : Kyle Stranick                                 #
#Class : ITN160                                         #
#Class Section : 401                                    #
#Date : 9/19/2023                                       #
#Assignment:Assignment 4-Commission calculation program #
#Version : 2.03                                         #
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

def main():
    print('\nWelcome to the Sale Commission Calculation Program')
    # assigned variables to output string to cut length of sentence
    pos = 'The percentage of the sale was'  # pos means percentage of sale
    cos = 'the amount of the commission was'  # cos means commission of sale

    while True:

        try:
            percentage = 0  # added to initialize, kept getting error that percentage referenced before assignment
            # .upper() changes any input into uppercase
            product = input('\nWhat product was sold?\t(A,B,C)  or Q to quit: ').upper()
            if product == 'Q':
                print('\nGoodbye!')
                break

            if product not in ['A', 'B', 'C', 'Q']:  # Using if not to exempt any input not related to these strings
                print('Invalid option, please select A, B, ,C or Q.')
                continue

            amount = float(input('\nWhat was the sales amount?: '))
            if amount < 10000:
                print('Invalid amount. Please enter an amount of 10,000 or more.')
                continue

            if product == 'A':
                if 10000 <= amount <= 19999:
                    percentage = 5
                elif 20000 <= amount <= 39999:
                    percentage = 7.5
                elif amount >= 40000:
                    percentage = 9
            elif product == 'B':
                if 10000 <= amount <= 19999:
                    percentage = 6
                elif 20000 <= amount <= 39999:
                    percentage = 8
                elif amount >= 40000:
                    percentage = 10
            elif product == 'C':
                if 10000 <= amount <= 19999:
                    percentage = 3
                elif 20000 <= amount <= 39999:
                    percentage = 4.5
                elif amount >= 40000:
                    percentage = 5.5

            commission = (percentage * 0.01) * amount
            # output sentence
            print(f'\n{pos} {percentage}% and {cos} ${commission:.2f}.')

        except ValueError:
            print('You have not typed a valid selection.')


if __name__ == '__main__':
    main()
