#!/usr/bin/env python3

def happy_new_year():
    # Use a while loop to count down from 10 to 1
    countdown = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Happy New Year!")

def square_integers(int_list):
    # Use a list comprehension to return a list of squared integers
    return [x ** 2 for x in int_list]

def fizzbuzz():
    # Use a for loop to print numbers from 1 to 100 with FizzBuzz rules
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

