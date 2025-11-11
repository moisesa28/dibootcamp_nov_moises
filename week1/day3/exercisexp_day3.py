# Exercise 1: Converting Lists into Dictionaries
# Instructions
# You are given two lists. Convert them into a dictionary where the first
# list contains the keys and the second list contains the corresponding values.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

# Convert lists to dictionary
result_dict = dict(zip(keys, values))
print(result_dict)

print('---')
print('')

# Exercise 2: Cinemax #2
# Instructions
# Write a program that calculates the total cost of movie tickets for a
# family based on their ages.

# Family members’ ages are stored in a dictionary.
# The ticket pricing rules are as follows:
# Under 3 years old: Free
# 3 to 12 years old: $10
# Over 12 years old: $15

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
total_cost = 0
for name, age in family.items():
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
    total_cost += ticket_price
print('Total cost for the family is: $', total_cost)
print('')
print('---')
print('')

# Exercise 3: Zara
# Instructions
# Create and manipulate a dictionary that contains information about the Zara brand.
#Brand info:
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green

#Create a dictionary called brand with the provided data.
brand = {
'name': 'Zara',
    'creation_date': 1975,
    'creator_name': ('Amancio Ortega Gaona'),
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink', 'green'],
    }
}   
print(brand)
print('----------')
# Change the value of number_stores to 2.
brand['number_stores'] = 2
print(brand)
# Print a sentence describing Zara’s clients using the type_of_clothes key.
print()
# Add a new key country_creation with the value Spain.
brand['country_creation'] = 'Spain'
print(brand)
print('--------')
# Check if international_competitors exists and, if so, add “Desigual” to the list.
brand['international_competitors'].append('Desigual')
print(brand)
print('--------')
# Delete the creation_date key.
del brand['creation_date']
print(brand)
print('--------')
# Print the last item in international_competitors.
print(brand['international_competitors'][-1])
print('--------')
# Print the major colors in the US.
print(brand['major_color']['US'])
print('--------')
# Print the number of keys in the dictionary.
print(len(brand))
print('--------')
# Print all keys of the dictionary.
print(brand.keys())
print('--------')


#Bonus
#Create another dictionary called more_on_zara with creation_date and number_stores. 
more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000,
}
# Merge this dictionary with the original brand dictionary and print the result.
brand.update(more_on_zara)
print(brand)

print('--------')
print('')

#Exercise 4: Disney Characters
#Instructions
# You are given a list of Disney characters. Create three dictionaries
# based on different patterns as shown below:

#Character List:
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

#1. Create a dictionary that maps characters to their indices:
char_to_index = {char: index for index, char in enumerate(users)}
print(char_to_index)
print('')

#2. Create a dictionary that maps indices to characters:
index_to_char = {index: char for index, char in enumerate(users)}
print(index_to_char)
print('')


#3. Create a dictionary where characters are sorted alphabetically 
# and mapped to their indices:
char_abc = {char: index for index, char in enumerate(sorted(users))}
print(char_abc)
print('--------')
