#Functions
#A function is a reusable set of operations.
#Why Use Functions?
# Think of a function as a box that performs a task. We give it an input, and it returns an output. 
# We don’t need to write the instructions again for different inputs; we could call the function again.

#a sequence of commands that can be reused.
#example
# print('Welcome, user!')

#syntax of a func:
#def (special word in python to used) <name_of_function> (it can be empty or can have argument):
    #an intended block of code

#call the function by the name of it

def greetings():
    print('Welcome, user!')

greetings()

#arguments in functions:
#
def greetings(user_name):
    print(f'Welcome, {user_name}!')

greetings('Gandalf')

#default argument
def greetings(user_name='John Doe'):
    print(f'Welcome, {user_name}!')
greetings()
greetings('Frodo')  

#positional arguments: the position you enter the argument matters.
def greetings(user_name, language):
    language = 'EN'
    if language == 'PT':
        print(f'Bem-vindo, {user_name}!')
    elif language == 'IT':
        print(f'Benvenuto, {user_name}!')

  
greetings('Aragorn','PT')
greetings('Aragorn','JP')
#keyword arguments: we do not worry about the position of the argument.

#create a fucntion called country_info that receives a country name as argument
#and prints the capital of that country. Make the country name argument default
#Naboo. Its capital is Thead

def country_info(country='Naboo'):
    if country == 'Russia':
        print('Moscow')
    
    elif country=='USA':
        print('Washington, D.C')

    else:
        print('Thead')

country_info('Russia')


