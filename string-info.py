#!/usr/bin/env python3

message = input("Enter a message: ")

print("First character: ",message[0])
print("Last character: ",message[-1])
print("Middle character: ",message[round(len(message) / 2)])
print("Even index characters: ",message[::2])
print("Odd index characters: ",message[1::2])
print("Reversed Message: ",message[-1::-1])

message[0] = 'a'


