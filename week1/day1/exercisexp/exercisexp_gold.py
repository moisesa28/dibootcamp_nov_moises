#Exercise 1 : Hello World-I love Python
#Print the following output in one line of code:
#Hello world
#Hello world
#Hello world
#Hello world
#I love python
#I love python
#I love python
#I love python

print('Hello world\n' * 4)
print('I love Python\n' *4)


#Exercise 2 : What is the Season ?
#Ask the user to input a month (1 to 12).
#Display the season of the month received :
#Spring runs from March (3) to May (5)
#Summer runs from June (6) to August (8)
#Autumn runs from September (9) to November (11)
#Winter runs from December (12) to February (2)

choose_month = int(input('Please choose a month(1 to 12) '))


if choose_month > 2 and choose_month < 6:
    print('The season is spring.')
elif choose_month > 5 and choose_month < 9:
    print('The season is summer.')
elif choose_month > 8 and choose_month <12:
    print('The season is autumn.')
elif choose_month >= 1 and choose_month ==12:
    print('The season is very cold.')

