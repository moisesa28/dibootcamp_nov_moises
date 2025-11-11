# #Tuples

# #Tuples are immutable lists, which means items can’t be changed.
# #To create a tuple, use parentheses:

# tup = (1,2,3,4, 'happy birthday')
# print(tup)

# a,b,c,d,e = tup
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)

# #a,b=tup this gives an error

# a, *b = tup
# print(a)
# print(b)

# #sets
# s = set([1,2,2,2,5,6])
# print(s)
# s.add(10)
# print(s)

# #loops
# #Loops are a fundamental programming concept that allows you
# #to iterate over the items of a list or repeat a given action a defined or even infinite number of times.
# # Loops are a fundamental programming concept that allows you 
# # to iterate over the items of a list or repeat a given 
# # action a defined or even infinite number of times.

# # Loops are a fundamental programming concept that allows you to iterate over the items of a list or repeat a given
# # action a defined or even infinite number of times.

li = [12,15,264,234,12,577,109]

# for each item in my list:
#     do something 
for item in li:
    if item > 200:
         print(item)

mysum = 0

for item in li:
     mysum = mysum + item
     print('current sum:', mysum)

print('final sum:', mysum)

#wild loop
#checks a condition if that condition is true

i = 0
while i <10:
    print(i)
    i= i +1


runs = int(input('how many times should we run '))
i = 0

while i < runs:
    print(i)
    i = i + 1

# li = [12,345,34,10,5,89,560]

# j = 0

# while j< len(li):
#     print(li[j])
#     j = j +1

# password = 'secret'

# guess = input('What is the password? ')
# while guess != password :
#     print('Incorrect password, try again')
#     guess = input('What is the password ')

# print('Correct password')

#break
# secret_number = 4

# while True:
#   user_number = input('Guess the secret number: ')
#   if int(user_number) == secret_number:
#     print('Congrats! You win!')
#     break
#   else:
#     print('Wrong guess...')