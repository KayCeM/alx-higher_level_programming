#!/usr/bin/python3
def uppercase(str):
    results = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            results += chr(ord(char) -32)
        else:
            results += char
            return results
str = "best school 98 battery street"
uppercase = uppercase(str)
print(uppercase)
