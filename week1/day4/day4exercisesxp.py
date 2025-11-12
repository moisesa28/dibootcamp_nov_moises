#Exercise 1: What Are You Learning?

#Step 1: Define a Function
#Define a function named display_message().
#Step 2: Print a Message



def display_message(): #this is the function
    print('I am learning about functions in Python') #message to be displayed

display_message() #calling the function
print('') 
print('------------')
#Exercise 2: What’s Your Favorite Book?
#Goal: Create a function that displays a message about a favorite book.
#Step 1: Define a Function with a Parameter

def favor_book(title): #this is the function with a parameter
    print(f'One of my favorite books is {title}.') #message to be displayed

favor_book('The Hobbit') 
favor_book('The Little Mermaid') #calling the function with different arguments
print('') 
print('------------')
#Exercise 3: Some Geography
# Goal: Create a function that describes a city and its country.

# defining the funciont:
def describe_city(city, country='Unknown'): #defining the function with two parameters.
        print(f'{city} is in {country}.') #message to be displayed
        if city =='Tel Aviv':
            country = 'Israel'
        elif city == 'Berlin':
             country = 'Germany'
        elif city == 'London':
             country = 'England' #changed the values for city and country
     
describe_city('Tel Aviv','Israel')
describe_city('Berlin', 'Germany') #calling the function with different arguments
describe_city('London', 'England')
describe_city('Toronto',)

print('') 
print('------------')
#Exercise 4: Random
#Goal: Create a function that generates random numbers and compares them.

import random
#Create a function that accepts a number between 1 and 100 as a parameter.

def random_num(num):
    
    randomnum = random.randint(1,100)
    if num == randomnum:
        print('Succes')
    elif num != randomnum:
        print(f'Fail, {num} and {randomnum}  do not match!')


num = input('Choose a number between 1 and 100: ')

random_num(num)
print('') 
print('------------')

#Exercise 5: Let’s Create Some Personalized Shirts!

#Step 1: Define a Function with Parameters
def make_shirt(size, text): #defining the function with 2 parameters
     print(f'The size of this shirt is {size} and it says {text}') #summrary message

make_shirt('small', 'hello') #calling the function

#Modify the Function with Default Values
def make_shirts(size='large', text='I love Python'):
     if size == 'medium':
          print(f'The size of this shirt is {size} and it says I hate Python!')
     elif size == 'small':
          print(f'The size of this shirt is {size} and it says Python Rules!')
     else:
        print(f'The size of this shirt is {size} and it says {text}')


make_shirts('large')
make_shirts('small')
make_shirts('medium')
make_shirts('xxl')

print('') 
print('------------')

# Exercise 6: Magicians
#Modify a list of magician names and display them in different ways.

#llist of magicians names:
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel', 'Harry Potter']

#function displaying magician names:
#Inside the function, iterate through the list and print each magician’s name.
def show_magicians(magician_names): #function using the magician names as a parameter
        for name in magician_names:
                print(name)

show_magicians(magician_names) #displaying the list
print('')
#Create a Function to Modify the List and add the great after each name
def make_great(magician_names):
        for name in magician_names:
                print(name + ' the great') #added the text after the name
        
make_great(magician_names)
print('')
show_magicians(magician_names)

print('')
print('-----------------')

#Exercise 7: Temperature Advice
#Generate a random temperature and provide advice based on the temperature range.

#Step 1: Create the get_random_temp() Function
#Create a function called get_random_temp() 
# that returns a random integer between -10 and 40 degrees Celsius.
import random
def get_random_temp():
    return random.randint(-10, 40) #function returning a random integer between -10 and 40

#Create a function called main(). Inside this function:
# Call get_random_temp() to get a random temperature.
# Store the temperature in a variable and print a friendly message like:
# “The temperature right now is 32 degrees Celsius.” 
def main():
    temperature = get_random_temp() #Calls get_random_temp() and prints the temperature.
    return(f"The temperature right now is {temperature} degrees Celsius.")
print(main())
print('')
print('-----------------')
# Use if-elif-else statements to provide advice based on the temperature:
def main():
    temperature = get_random_temp()
    if temperature < 0:
        return f"It is {temperature} degrees Celsius. Brrr, that's freezing! Wear some extra layers today."
    elif 0 <= temperature < 16:
        return f"It is {temperature} degrees Celsius. Quite chilly! Don't forget your coat."
    elif 16 <= temperature < 23:
        return f"It is {temperature} degrees Celsius. Nice weather."
    elif 24 <= temperature < 32:
        return f"It is {temperature} degrees Celsius. A bit warm, stay hydrated."
    else:
        return f"It is {temperature} degrees Celsius. It's really hot! Stay cool."
print(main())


