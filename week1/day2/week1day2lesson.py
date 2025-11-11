# #Sequences, List, Sets, Tuple

# #LISTS
# #Lists let you store a collection of items. These items can be of any type: integers, strings, booleans or even other lists.

# my_list = ['apple','banana','Book',1234, True]

# #To access the items, refer to the index number.
# my_list[0] #first item on the list
# my_list[-1] #the last item on the list, it is negative counting from the end to the beginning

# #Modify an element
# #The list is mutable; it means that the contents of a list can be updated. 
# #To change an element in a list, refer to the index number and assign a new value.

# print(my_list)
# my_list[1] = 'grape'
# print(my_list)

# #Add an element
# #Adding an element to a list is called appending.

# #To append an item to a list, use the append() method.

# my_list.append('coffe')
# print(my_list)

# #Remove an element
# #To remove a specified item, use the remove method; this method removes the first occurrence of the element.
# my_list.remove('apple')

# #To remove an item by its index, use the pop method; this method removes the element at the given index and returns it.
# my_list.pop(1)

# #Adding two lists
# #Adding two lists will concatenate them.

# first = [1,2,3,4]
# second = [5,6,7,8]

# first.extend (second)

# print(first +second)

# #List functions
# #Length
# #Using the len() function allows to retrieve the number of items contained in a given list.
# #Sum
# #If you have a list of numbers, you can get the sum of all numbers again through a function.
# #Sorting
# #There are different ways of sorting elements of a list, sorted() lets you straightforwardly do that.
# #If you have strings, they will get sorted alphabetically.

# #More methods

# food = ['spam', 'eggs', 'ham']
# food.append('sushi')
# print(food)
# #>> ['spam', 'eggs', 'ham', 'sushi']

# food.insert(0, 'beans')
# print(food)
# #>> ['beans', 'spam', 'eggs', 'ham', 'sushi']

# food.extend(['bread', 'water'])
# print(food)
# #>> ['beans', 'spam', 'eggs', 'ham', 'sushi', 'bread', 'water']

# #exercise1
# list1 = [5, 10, 15, 20, 25, 50, 20]

# list1[3] = 200
# print(list1)


