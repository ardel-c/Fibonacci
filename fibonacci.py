#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 22:28:54 2020

@author: ardeliachristina
"""


import math

# Fibo sequence starting from f(0): 0,1,1,2,3,5,8,13,22, ...

def is_perfect_square(number):
    x = math.sqrt(number)
    return(x**2 == number)
    
def is_fibo(is_fibo):
    if is_perfect_square(5*is_fibo**2 + 4):
        return True
    elif is_perfect_square(5*is_fibo**2 - 4):
        return True
    else:
        return False
    
def f(nth_fibo):    
    if nth_fibo <= 1:
        return nth_fibo
    return f(nth_fibo-1) + f(nth_fibo-2)

session = 1
while session == 1:
    print("\n\nWelcome to Fibonacci Program")
    print("1. Find nth Fibonacci term")
    print("2. Check if number is in Fibonacci sequence")
    print("3. Exit")
    input_menu = input("Enter your input (1|2|3): ") 
    
    if int(input_menu) == 1:
        input_calc = input("Fibonacci term to find: ") 
        result_calc = f(int(input_calc))
        print("The " + str(input_calc) + "th term in Fibonacci is " + str(result_calc))
        cont = input("Press enter to continue.") 
    elif int(input_menu) == 2:
        input_check = input("Enter number to check: ") 
        result_check = is_fibo(int(input_check))
        if(result_check):
            result_check_wording = "in Fibonacci sequence"
        else:
            result_check_wording = "not in Fibonacci sequence"
        print("The number " + input_check + " is " + result_check_wording)
        cont = input("Press enter to continue.") 
    elif int(input_menu) == 3:
        session=0
    else:
        print("Invalid input")

