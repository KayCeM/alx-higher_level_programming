#!/usr/bin/python3
for x in range(0, 10):
    for y in range(x+1, 10):
        if x != y:
            if x == 8 and y == 9:
                print('89')
            else:
                print(f'{x}{y}, '.format(x, y), end='')
