#Daily Challenge: Dictionaries
#Challenge 1: Letter Index Dictionary
# Goal: Create a dictionary that stores the indices (number of the position)
#  of each letter in a word provided by the user(input()).
# Instructions:

# 1. User Input:
# Ask the user to enter a word.
# Store the input word in a variable.
word = input('Please enter a word: ')

# 2. Creating the Dictionary:

# Iterate through each character of the input word using a loop.
# And check if the character is already a key in the dictionary.
# If it is, append the current index to the list associated with that key.
# If it is not, create a new key-value pair in the dictionary.
# Ensure that the characters (keys) are strings.
# Ensure that the indices (values) are stored in lists.
letter_index_dict = {}
for index, char in enumerate(word):
    if char in letter_index_dict:
        letter_index_dict[char].append(index)
    else:
        letter_index_dict[char] = [index]

print(letter_index_dict)
print('-------- ')
print('')

#Challenge 2: Affordable Items
#Goal: Create a program that prints a list of items that
# can be purchased with a given amount of money.
#Instructions:
# 1. Store Data:
# You will be provided with a dictionary (items_purchase) where the keys are the item names and the values are their prices (as strings with a dollar sign). The priority is defined by the position of the iten on the dictionary: from the most important to the less important.
# You will also be given a string (wallet) representing the amount of money you have.
items_purchase = {
    "Laptop": "$999",
    "Headphones": "$199",
    "Mouse": "$49",
    "Keyboard": "$89",
    "Monitor": "$299",
    "USB Cable": "$19"
}
wallet = "$250"
print('')

#2. Data Cleaning:
# You need to clean the dollar sign and the commas using python. Don’t hard code it.
wallet_amount = float(wallet.replace('$', '').replace(',', '')) 
print(f'Wallet amount: {wallet_amount}')
print('')   

#3. Determining Affordable Items:
# create a list called basket and add there the items that you can buy with the money you have on the wallet
# Don’t forget to update the wallet after buying an item.
# If the basket is empty (no items can be afforded), return the string “Nothing”.
# Otherwise, print the basket list in alphabetical order.
basket = []
for item, price in items_purchase.items():
    item_price = float(price.replace('$', '').replace(',', ''))
    if item_price <= wallet_amount:
        basket.append(item)
        wallet_amount -= item_price

if not basket:
    print("Nothing")
else:
    print(sorted(basket))   

print('-------- ')

items_purchase1 = {
    "Water": "$1", 
    "Bread": "$3", 
    "TV": "$1,000", 
    "Fertilizer": "$20",
    }
wallet = "$300"

#Data Cleaning
wallet_amount = float(wallet.replace('$', '').replace(',', '')) 
print(f'Wallet amount: {wallet_amount}')
print('')   
#Determining Affordable Items   
basket = []
for item, price in items_purchase1.items():
    item_price = float(price.replace('$', '').replace(',', ''))
    if item_price <= wallet_amount:
        basket.append(item)
        wallet_amount -= item_price

if not basket:
    print("Nothing")
else:
    print(sorted(basket))   
print('-------- ')
items_purchase3 = {
    "Apple": "$4", 
    "Honey": "$3", 
    "Fan": "$14", 
    "Bananas": "$4", 
    "Pan": "$100", 
    "Spoon": "$2",
    }
wallet = "$100"
#Data Cleaning
wallet_amount = float(wallet.replace('$', '').replace(',', '')) 
print(f'Wallet amount: {wallet_amount}')
print('')   
#Determining Affordable Items   
basket = []
for item, price in items_purchase3.items():
    item_price = float(price.replace('$', '').replace(',', ''))
    if item_price <= wallet_amount:
        basket.append(item)
        wallet_amount -= item_price

if not basket:
    print("Nothing")
else:
    print(sorted(basket))   
print('-------- ')
print('')

items_purchase4 = {
    "Phone": "$999",
    "Speakers": "$300", 
    "Laptop": "$5,000", 
    "PC": "$1200",
    }
wallet = "$1"
#Data Cleaning
wallet_amount = float(wallet.replace('$', '').replace(',', '')) 
print(f'Wallet amount: {wallet_amount}')
print('')
#Determining Affordable Items   
basket = []
for item, price in items_purchase4.items():
    item_price = float(price.replace('$', '').replace(',', ''))
    if item_price <= wallet_amount:
        basket.append(item)
        wallet_amount -= item_price

if not basket:
    print("Nothing")
else:
    print(sorted(basket))         
print('-------- ')