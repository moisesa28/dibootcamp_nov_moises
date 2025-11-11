#Loops and Dictionaries
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

#loop in a list:
for item in student_info1:
    print(item)

#options of loops in a dictionary:

#access only the keys = keys()
for keys in student_info.keys():
    print(keys)

#access the values = values()
for values in student_info.values():
    print(values)

#access both 
for keys, values in student_info.items():
    print(keys,values)

#we want to change all the sting values to uppercase:
for keys, values in student_info.items():
    if type(values) == str:
        student_info[keys] = values.upper()

print(student_info)

