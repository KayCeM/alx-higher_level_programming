#!/usr/bin/python3
def uppercase(str):
    results = " "
    for char in str:
        if 97 <= ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
            return results
str = "Best School 98 Battery street"
uppercase = uppercase(str)
print(uppercase)
