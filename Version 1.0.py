#########################################################
#Author : Kyle Stranick                                 #
#Class : ITN160                                         #
#Class Section : 401                                    #
#Date : 9/12/2023 finished 9/14/23                      #
#Assignment:Assignment 4-Commission calculation program #
#Version : 1.02                                         #
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
#Version 1.01: implementation of [if not] to negate any inputs that are not (A,B,C)
#Version 1.01: implementation of return to end program with invalid inputs
#Version 1.02: implementation of if amount < 10000 to negate any value less than 10000


def main():
    print('\nWelcome to the Sale Commission Calculation Program')

    product = input('\nWhat product was sold?\t(A,B,C): ').upper()  # .upper() changes any input into uppercase
    if product not in ['A', 'B', 'C']:
        print('Invalid option, please select A, B, or C.')
        return

    amount = float(input('What was the sales amount? '))
    if amount < 10000:
        print('Invalid amount. Please enter an amount of 10,000 or more.')
        return

    if product == "A":
        if 10000 <= amount <= 19999:
            percentage = 5
        elif 20000 <= amount <= 39999:
            percentage = 7.5
        else:
            percentage = 9
    elif product == "B":
        if 10000 <= amount <= 19999:
            percentage = 6
        elif 20000 <= amount <= 39999:
            percentage = 8
        else:
            percentage = 10
    else:
        if 10000 <= amount <= 19999:
            percentage = 3
        elif 20000 <= amount <= 39999:
            percentage = 4.5
        else:
            percentage = 5.5

    commission = (percentage * 0.01) * amount

    print(f'\nThe percentage for the sale was {percentage}% and the amount of the commission was ${commission:.2f}.')


if __name__ == '__main__':
    main()
