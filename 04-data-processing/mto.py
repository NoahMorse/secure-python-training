#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise #2


Write a script that will:
    1. Add a new order that includes at least two items
    2. Replace the mozarella-sticks in Jane's classic-sample with jalapeno-popperz
    3. Write the updated order to a new file
    3. Total all four orders, print the result

"""
import json
from pprint import pprint

f = open('sheetz-order.json')
orders = json.load(f)
f.close()