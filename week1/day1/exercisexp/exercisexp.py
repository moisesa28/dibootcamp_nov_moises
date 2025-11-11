#Exercise 1: Hello World
#Instructions
#Print the following output using one line of code:
#Hello world
#Hello world
#Hello world
#Hello world

print('Hello world\n' *3)


#Exercise 2: Some Math
#Instructions:
#Write code that calculates the result of:
#(99^3)*8 (meaning 99 to the power of 3, times 8).
cube = (99*99*99)
cube = (99**3)
print(cube *8)

#Exercise 3: What is the output?
#Instructions
#Predict the output of the following code snippets:
#Coment what is your guess, then run the code and compare
#Example:
#>>> 15 < 8 #False

#>>> 5 < 3  #False 
#>>> 3 == 3 #True
#>>> 3 == "3" #False error
#>>> "3" > 3 #False error
#>>> "Hello" == "hello" #False


#Exercise 4: Your computer brand
#Instructions
#Create a variable called computer_brand which value is the brand name of your computer.
#Using the computer_brand variable, print a sentence that states the following:
#"I have a <computer_brand> computer."

computer_brand = 'Mojojojo'
print(f'I have a {computer_brand} computer.')


#Exercise 5: Your information
#Instructions
#Create a variable called name, and set it’s value to your name.
#Create a variable called age, and set it’s value to your age.
#Create a variable called shoe_size, and set it’s value to your shoe size.
#Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2, and 3.
#Have your code print the info message.
#Run your code.

name = "Moises"
age = 40
shoe_size = 43
info = (f'My name is {name} and I\'m {age} years old and my shoe size is {shoe_size}, but I actually do not wear shoes')
print(info)

#Exercise 6: A & B
#Create two variables, a and b.
#Each variable’s value should be a number.
#If a is bigger than b, have your code print "Hello World".

a = 17
b = 13

if a>b:
    print('Hello world.')

elif a<b:
    print('Goodbye world!')

#Exercise 7: Odd or Even
#Write code that asks the user for a number and determines whether this number is odd or even.

choose_number = int(input('Choose a number '))

if choose_number % 2 == 0:
    print('Even')
if choose_number % 2 != 0:
    print('Odd')

#Exercise 8: What’s your name?
#Write code that asks the user for their name and
#determines whether or not you have the same name.
#Print out a funny message based on the outcome.

user_name = input('What is your name ')

if user_name == 'Moises':
    print('Oh, your name is the Best!')

elif user_name != 'Moises':
    print('I am sorry about your awful name')


#Exercise 9: Tall enough to ride a roller coaster
#Write code that will ask the user for their height in centimeters.
#If they are over 145 cm, print a message that states they are tall enough to ride.
#If they are not tall enough, print a message that says they need to grow some more to ride.

height_cm = input('What is your heigh in cm ')

if height_cm > '145'and height_cm <= '175':
    print('You are tall enough to ride, please come in.')

if height_cm <='145':
    print('You need to take vitamins to grow more, bye bye.')

elif height_cm >= '175':
    print('You are too tall for this ride, please step down.')

 


