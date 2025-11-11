# #Exercise 1: Favorite Numbers
# Create a set called my_fav_numbers and populate it with your favorite numbers.
# Add two new numbers to the set.
# Remove the last number you added to the set.
# Create another set called friend_fav_numbers and populate it with your friend’s favorite numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to create a new set called our_fav_numbers.
# Note: Sets are unordered collections, so ensure no duplicate numbers are added.

my_fav_numbers = set([5,7,13,21,23,28,36,48])
print(my_fav_numbers)
print('----------')
my_fav_numbers.add(69)
my_fav_numbers.add(91)
print(my_fav_numbers)
print('----------')
my_fav_numbers.remove(91)
print(my_fav_numbers)
print('----------')
friend_fav_numbers = set([2,8,11,32,54,66])
print(friend_fav_numbers)
print('----------')
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)
print('----------------\n')
#Exercise 2: Tuple
# Instructions:
# Given a tuple of integers, try to add more integers to the tuple.
# Hint: Tuples are immutable, meaning they cannot be changed after creation. Think about why you can’t add more integers to a tuple.
mytup = (1,2,3,4,5,6)
print(mytup)
a,b,c,d,e,f = mytup
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print('')
      
print('You cannot add more integers to the tuple since the integers set on a tuple cannnot be modified or change')
print('')

# Exercise 3: List Manipulation
# Instructions:
# You have a list: basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(basket)
print('')

# Remove "Banana" from the list.
basket.pop(0)
print(basket)
print('')
# Remove "Blueberries" from the list.
basket.pop(-1)
print(basket)
print('')
# Add "Kiwi" to the end of the list.
basket.append("kiwi")
print(basket)
print('')
# Add "Apples" to the beginning of the list.
basket.insert(0,'Apples')
print(basket)
print('')
# Count how many times "Apples" appear in the list.
print('How many times "Apples" appear in the list.')
print(basket.count('Apples')) 
print('')
# Empty the list.
basket.clear()
print(basket)
print('---------')

# Print the final state of the list.
print(basket)

# Exercise 4: Floats
# Instructions:
# Recap: What is a float? What’s the difference between a float and an integer?
# Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5.
# Avoid hard-coding each number manually.
# Think: Can you generate this sequence using a loop or another method?
list4 = [1.5,2,2.5,3,3.5,4,4.5,5]


print('----------------')
#Exercise 5: For Loop
# Instructions:
# Write a for loop to print all numbers from 1 to 20, inclusive.

thislist = range(1,21)
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
# Write another for loop that prints every number from 1 to 20 where the index is even.
print('-----------')
for i in range(1, 21):
  if i % 2 == 0:
    print(i)

print('')
print('-----------------')
#Exercise 6: While Loop
# Instructions:
# Use an input to ask the user to enter their name.
# Using a while True loop, check if the user gave a proper name (not digits and at least 3 letters long)
# hint: check for the method isdigit()
# if the input is incorrect, keep asking for the correct input until it is correct
# if the input is correct print “thank you” and break the loop

while True:
    name = input("Please enter your name: ")
    if not name.isdigit() and len(name) > 3:
        print("thank you")
        break
    else:
        print("Invalid input. Please enter a name with at least 3 letters and no digits.")

print('')
print('---------------')

#Exercise 7: Favorite Fruits
# Instructions:
# Ask the user to input their favorite fruits (they can input several fruits, separated by spaces).
# Store these fruits in a list.
# Ask the user to input the name of any fruit.
# If the fruit is in their list of favorite fruits, print:
# "You chose one of your favorite fruits! Enjoy!"
# If not, print:
# "You chose a new fruit. I hope you enjoy it!"

users_fav_fruits = input('What are your favorite fruits? ')

fruitlist = users_fav_fruits.split(' ')

fruit1 = input('What fruit did you eat today? ')
if fruit1 in fruitlist:
       print('You chose one of your favorite fruits! Enjoy!')
if fruit1 not in fruitlist:
    print('You chose a new fruit. Hope you enjoy it!')


print('')
print('--------------')
#Exercise 8: Pizza Toppings
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.

toppings = []
base_price = 10
topping_price = 2.50

while True:
    topping = input("Enter a pizza topping (or type 'quit' to finish): ")
    if topping == 'quit':
        break
    else:
        toppings.append(topping)
        print(f"Adding {topping} to your pizza.")
total_cost = base_price + len(toppings) * topping_price
print(f"Base Price: ${base_price:.2f}")
print(f"Total Topping Cost: ${len(toppings) * topping_price:.2f}")
print(f"Total Cost: ${total_cost:.2f}")

print('')
print('----------------')

#Exercise 9: Cinemax Tickets
# Instructions:
# Ask for the age of each person in a family who wants to buy a movie ticket.
# Calculate the total cost based on the following rules:
# Free for people under 3.
# $10 for people aged 3 to 12.
# $15 for anyone over 12.
# Print the total ticket cost.

total_cost = 0

while True:
    age_input = input("Enter the age of a family member (or type 'quit' to finish): ")
    if age_input.lower() == 'quit':
        break
    try:
        age = int(age_input)
        if age < 0:
            print("Please enter a valid age.")
            continue
        elif age < 3:
            cost = 0
            print(f"Age {age}: Free")
        elif age <= 12:
            cost = 10
            print(f"Age {age}: ${cost}")
        else:
            cost = 15
            print(f"Age {age}: ${cost}")
        total_cost += cost
    except ValueError:
        print("Invalid input. Please enter a number or 'quit'.")

print(f"\nTotal ticket cost: ${total_cost}")

