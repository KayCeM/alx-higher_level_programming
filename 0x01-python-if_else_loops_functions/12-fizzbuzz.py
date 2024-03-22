#!/usr/bin/python3
for count in range(1, 101):
    if count in range(15, 101, 15):
        print("FizzBuzz" .format(count), end=" ")
    if count in range(3, 101, 3):
        print("Fizz " .format(count), end=" ")
    elif count in range(5, 101, 5):
        print("Buzz " .format(count), end=" ")
    else:
        print(count, end=" ")
