#! /usr/local/bin/python3

from datetime import date
print("Hello, This is an introduction to get your names !!!")

name  = input("What is your name? : ")
color = input("What is your favorite color? : ")
#age = int(input("How old are you today? : "))
birthdate = input("What is your date of birth? (dd/mm/yyyy)? : ")

today = date.today()
#d1 = date.strftime(birthdate,"%d/%m/%YY")
bdate = birthdate.split("/")

age =  today.year - int(bdate[2]) - ((today.month, today.day) < (int(bdate[1]), int(bdate[0])) ) 

#print("\nYour name : " + name + "\nFavorite Color : " + color + "\nAge : " + str(age) + " years\n")
print (name, "is", age ,"years old and loves the color", color + ".", sep=" ")