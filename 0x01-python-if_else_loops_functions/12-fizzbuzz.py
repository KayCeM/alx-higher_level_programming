#!/usr/bin/python3
for count in range(1, 101):
    if count in range(15, 101, 15):
        print("FizzBuzz", end=" ")
    if count in range(3, 101, 3):
        print("Fizz ", end=" ")
    elif count in range(5, 101, 5):
        print("Buzz ", end=" ")
    else:
        print(count, end=" ")
        continue
        print()
