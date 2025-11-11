# Instructions:
# 1. Ask the user for two inputs:

# A number (integer).
# A length (integer).

# 2. Create a program that generates a list of multiples of the given number.
# 3. The list should stop when it reaches the length specified by the user.


number = int(input('Type in a number '))

length = int(input('Choose a lenght '))

multiples = [number * i for i in range(1, length + 1)]
print(multiples)

   
print('')
print('------------')

# Challenge 2: Remove Consecutive Duplicate Letters
#1. Ask the user for a string.

word = str(input('Type a word  \n'))
result =''
for char in word:
    if not result or char != result[-1]:
        result += char
print(result)
    
