#!/usr/bin/env python3.7

values = int(input("How many values should we process: ")) + 1


for i in range(1,values):
    
    if not i%15:
        print("FizzBuzz")
    elif not i%3:
        print("Fizz")
    elif not i%5:
        print("Buzz")
    else:
        print(i)


