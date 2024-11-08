# -*- coding: utf-8 -*-
"""
Functions Exercise


Write a script that calls 5 unique functions. Here's what each function should do:
    
    1. get_employee_information()
      - Should prompt the employee for their Name, Hourly Pay, and Hours Worked
      - Should return all three values
    
    2. calculate_overtime_hours()
      - Should take in the hours worked as an argument
      - Should return two values. Non-overtime hours and overtime hours (If no overtime hours, return 0)
      
    3. calculate_standard_pay()
      - Should take in the non-overtime hours and hourly_pay values, and return the calculated standard pay
      
    4. calculate_overtime_pay()
      - Should take in the overtime hours and hourly_pay values
      - Should calculate overtime pay as time and a half
      - Should ONLY be called if there are overtime hours
      
    5. display_total_pay()
      - Should take in the name, overtime pay, and standard pay
      - Should sum the standard and overtime pay
      - Should print out the following:
          "The weekly pay for <name> is $<amount>."

"""




def get_employee_information():
    name = input("What is your name? ")
    hours = int(input("How many hours did you work? "))
    hourly_pay = float(input("What is your hourly pay? "))
    return name, hours, hourly_pay

def calculate_overtime_hours(hours_worked):
    if hours_worked <= 40:
        return hours_worked, 0
    return 40, hours_worked - 40

def calculate_standard_pay(hours, hourly_pay):
    return hours * hourly_pay
    
def calculate_overtime_pay(hours, hourly_pay):
    return hourly_pay * 1.5 * hours

def display_total_pay(name, standard_pay, overtime_pay):
    total_pay = standard_pay + overtime_pay
    print(f"The weekly pay for {name} is ${total_pay:.2f}")





name, hours, hourly_pay = get_employee_information()

hours, overtime_hours = calculate_overtime_hours(hours)

standard_pay = calculate_standard_pay(hours, hourly_pay)

overtime_pay = 0
if overtime_hours:
    overtime_pay = calculate_overtime_pay(hourly_pay, overtime_hours)

display_total_pay(name, standard_pay, overtime_pay)

