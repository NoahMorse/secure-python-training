# -*- coding: utf-8 -*-
"""
Exercise #1

Write a script that will prompt a user for their:
    1. Name
    2. Hourly Pay
    3. Hours worked

It should then calculate what the weekly pay is, and print out:
    "The weekly pay for <name> is $<amount>."
    
Bonus: Calculate any over-time pay as time and a half

"""

name = input("What is your name? ")
hours = int(input("How many hours did you work? "))
hourly_pay = float(input("What is your hourly pay? "))
