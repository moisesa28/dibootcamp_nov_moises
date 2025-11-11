#BASIC DATA TYPES

#STRING
#its shows it is a string when it has quotation marks. it can be single or double.
#it is a text in python written inbetween quotaions marks. It is a sequience of characters
#upper() changes to upper case
#lower(). changes to lower case
#len() length of the string

description = "strings are..."
#make it all uper case
print (description.upper())

#replace the word "are" to "is"
print(description.replace('are', 'is'))

#print just the word "strings"
print(description[:7])


#VARIABLES
f_name = 'Harry'
l_name = 'Potter'
age = 15
address = 'Private Drive 4'
is_wizard = True

#How to name variable, best practices. 
# Don't use numbers or special character.
#use short names, underscore _ as a space

x = 1
y = 2

#try to sawp the values of x and y
#correct code
temp = y
y = x
x = temp
print(x,y)

#useful function:
#print() - it shows something define on the parenthesis on the terminal
#input() - prompt the user for some info

#user_name = input('Enter your name: ')
#print(user_name)

#the inputed info comes as a str

#age = int(input('enter your age:'))
#print (age)

#print(f'{suer_name} is {age} years old')

#f strings = the f stands for format, 
# everything that is a variable goes between {}

#increment a variable
#count = orcount +=1
#print(user_name)
#print(count)

#exercise 2 
#Ask the user for their age using the input() function and store it in a variable age.

#Convert the inputted age into an integer and calculate the number of years until they turn 100.
#Display a message: "You will turn 100 in X years", where X is the number of years calculated.

user_age = int(input('What is your age'))
x = 100 - user_age
print(f'You will turn 100 in {x}')

