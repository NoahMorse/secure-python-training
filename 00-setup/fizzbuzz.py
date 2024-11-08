# -*- coding: utf-8 -*-
"""
FizzBuzz exercise:
    
    Write a program that prints the numbers from 1 to 100.

    For multiples of three, print "Fizz" instead of the number.
    For multiples of five, print "Buzz" instead of the number.
    For numbers which are multiples of both three and five, print "FizzBuzz".

"""

#FizzBuzz 1

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#FizzBuzz 2    
myStr = ""
for i in range(1, 101):
    if i % 3 == 0:
        myStr += "Fizz"
    if i % 5 == 0:
        myStr += "Buzz"
    print(myStr) if myStr else print(i)
    myStr = ""
        