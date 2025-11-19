#Exercise 1: Currencies
#Implement dunder methods for a Currency class to handle string representation, 
# integer conversion, addition, and in-place addition.

print('Exercise 1: Currencies')
print('')

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f'{self.amount} {self.currency}'
    

    def __repr__(self):
        return f"Currency('{self.currency}', {self.amount})"

    def __int__(self):
        return int(self.amount)
        

    def __add__(self, other):
        if isinstance(other,Currency):
            if self.currency == other.currency:
                return Currency(self.currency, int(self.amount + other.amount))
            return self
        

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise ValueError("Cannot add two different currencies.")
            self.amount += other.amount
            return self
        

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1) 
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

# c1 += c2
print(c1)
# 20 dollars

# print(c1 + c3)
# TypeError: Cannot add between Currency type <dollar> and <shekel>


print('_____________')
print('')
# Exercise 2: Import
print('Exercise 2: Import')
print('')
from func import sum
sum(2,4)
sum(4,4)
sum(5,5)

print('_____________')
print('')

#Exercise 3: String module
print('Exercise 3: String module')
print('')
#Generate a random string of length 5 using the string module.
#Use the string module to generate a random string of length 5,
#consisting of uppercase and lowercase letters only.

#Import the string and random modules.
import string
import random

#string of letters:
all_letters = string.ascii_letters
print(all_letters)

# Generate a random string
random_string = ''.join(random.choice(all_letters) for i in range(5))
print(random_string)
print('_____________')
print('')
# Exercise 4: Current Date
print('Exercise 4: Current Date')
print('')
#Use the datetime module to create a function that displays the current date.
from datetime import date

#Get the current date
def display_current_date():
    today = date.today()
    current_day = today.strftime('%b %d, %Y')
    print("The current date is", current_day)

# Display the date
display_current_date()

print('_____________')
print('')
# Exercise 5: Amount of time left until January 1st
print('Exercise 5: Amount of time left until January 1st')
print('')

#Create a function that displays the amount of time left until January 1st.
# def time_left_january_first():
from datetime import datetime

#Get the current date and time
def display_current_datetime():
    now = datetime.now()
    current_datetime = now.strftime('%B %d, %Y %H:%M:%S')
    print("The current date and time is", current_datetime)

#Create a datetime object for January 1st of the next year
def time_left_next_year():
    now = datetime.now()
    current_year = now.year
    next_year = (current_year + 1)
    next_new_year = datetime(next_year, 1, 1,)
    time_difference = next_new_year - now

    print("Time until January 1st of next year:", time_difference)

display_current_datetime()
time_left_next_year()

print('_____________')
print('')
# Exercise 6: Birthday and minutes
print('Exercise 6: Birthday and minutes')
print('')
#Create a function that accepts a birthdate as an argument (in the format of your choice), 
# then displays a message stating how many minutes the user lived in his life.

def calculate_minutes_lived(birthdate_str):
    try:
        # Convert birthdate string to a datetime object
        birthdate = datetime.strptime(birthdate_str, '%d-%m-%Y')

        # Get the current datetime
        now = datetime.now()

        # Calculate the time difference
        time_difference = now - birthdate

        # Convert the time difference to total minutes
        total_minutes = int(time_difference.total_seconds() / 60)

        print(f"You have lived approximately {total_minutes} minutes in your life.")
    except ValueError:
        print("Invalid birthdate format. Please use 'DD-MM-YYYY'.")


calculate_minutes_lived('28-04-1985')
calculate_minutes_lived('24.4.85')

print('_____________')
print('')
# Exercise 7: Faker Module
print('Exercise 7: Faker Module')
print('')

# Use the faker module to generate fake user data and store it in a list of dictionaries.

from faker import Faker

def generate_fake_users(num_users):
    fake = Faker()
    users = []
    for _ in range(num_users):
        user = {
            'name': fake.name(),
            'address': fake.address(),
            'language_code': fake.language_code()
        }
        users.append(user)
    print(users)

generate_fake_users(3)
