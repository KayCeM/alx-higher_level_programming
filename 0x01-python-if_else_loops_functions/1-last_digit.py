#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = number % 10
if string > 5:
    print("Last digit of {0} is {1} and is greater than 5".format(number, string))
elif string == 0:
    print("Last digit of {0} is {1} and is 0".format(number, string))
elif string < 6 and string > 0:
    print("Last digit of {0} is {1} and is less than 6 and not 0".format(number, string))
