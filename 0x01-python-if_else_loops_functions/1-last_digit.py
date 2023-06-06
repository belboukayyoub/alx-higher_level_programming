#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1]) if number > 0 else int(str(number)[-1]) * -1
msg = f"Last digit of {number} is {last_digit}"
if last_digit > 5:
    msg += " and is greater than 5"
if last_digit == 0:
    msg += " and is 0"
elif last_digit < 6:
    msg += " and is less than 6 and not 0"
print(msg)
