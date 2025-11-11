#conditionals
#are a universal programming paradigm to take specific 
#actions based on data comparison.
#if something is true, then perform such action, otherwise perform another action.

#logic operators:
print(5 == '5') #equals
print(5!='5') #different
print(5<3) #less than
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b


#syntax of conditional expression:

#if <condition>:
#   an indented block of code

user_age = int(input('what is your age'))

if user_age < 12:
    print('Sorry, you can\'t see the movie')

elif user_age >= 13 and user_age <= 16:
    print('You can see the movie with your parents')
else:
    print('You can see the movie')