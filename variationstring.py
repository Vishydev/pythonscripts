#!/usr/bin/env python3.7

message = input("Enter a message: ")

print("Lowercase: " + message.lower())
print("Uppercase: " + message.upper())
print("Capitalised: " + message.capitalize())
print("Title Case: " + message.title())

#print("Words : {}".format( message.split(" ")))
#another way
print("Words :",message.split()) # am empty split  will take all whitespaces including tab


#print("Aphabetic First Word",message.find())

words = message.split()
sortedwords = sorted(words)
print(words)
print(sortedwords)
print("Alphabetic First Word:", sortedwords[0])
print("Alphabetic Last Word:", sortedwords[-1])
