# Dictionaries

# Complex Data Structure:

# Dictionary is a data type provided by python, which is another collection of objects.
# A dictionary is similar to a list, in many ways:
# It’s mutable (his elements can be changed)
# It’s dynamic (it can grow as needed)
# Dictionaries are an unordered collection of items that store values on a key-value pair basis.
# With a dictionary, you create a structured piece of data and retrieve values using a key.
# You can think of them as a spreadsheet table: you have columns with names (keys) and cells with data (values).

student_info1 = ['Harry', 'Potter', 15, 'Private Drive, 4', 'Hedwig', 'Buckbeak']

student_info = {
    'first_name': 'Harry',
    'last_name': 'Potter',
    'age': 15,
    'address': 'Private Drive, 4',
    'pets': ['Hedwig', 'Buckbeak'],
    'best_friends': ('Ron Weasley', 'Hermione Granger'),
    'is parselmouth': True,
    'Houses': {'main': 'Gryffindor', 'second': 'Slytherin', 'third': 'Hufflepuff', 'fourth': 'Ravenclaw'},
    }


print(student_info1[0])

print(student_info['first_name'])
student_info['pets'].append('Toby')

#Changing values in a dictionary
# student_info['age'] = 16
# print(student_info)

#exercise
#print harry's age
#add 10 year to age and print again
print(student_info['age'])
student_info['age'] += 10
print(student_info['age'])

#change the address to Bezalel 8
student_info['address'] = 'Bezalel 8'

#add a new pet
student_info['pets'].append('Crookshanks')

#change is parselmouth to False
student_info['is parselmouth'] = False
print(student_info)


#how to add a new key value pair in a dictionary
student_info['wand'] = 'Holly, 11", phoenix feather' #option1
student_info.update({'principal':'Dumbledore'}) #option2
print(student_info)

#How to delete a key value pair from a dictionary
del student_info['address'] 
print(student_info)


# Exercise2
#Access the value of key history

sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict['class']['student']['marks']['history']) #correct


#BRACKETS:
#() - methods, functions, tuples, structures
#[] - lists, indexing
#{} - dictionaries, sets

#Accesing data

# Difference between dictionaries and lists
# How elements are accessed:
# In lists, elements are accessed by their position in the list (via indexing)
# In dictionaries, elements are accessed via keys