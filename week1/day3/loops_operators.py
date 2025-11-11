student_info1 = ['Harry', 'Potter', 15, 'Private Drive, 4', 'Hedwig', 'Buckbeak']
#Loops Operators
# range(start, stop[, step]) : iterator in loops.

#syntax for loops:

#for <variable> in <sequence>:
    #will happen withing each iteration

#range() - helps to create a sequence of numbers
#range(start number, stop number, steps)
for num in range(1,11):
    print(num)

for num in range(1,11,2):
    print(num)

#enumerate(iterable) : enumerate each item in the iterable
#gives us a tuple with index and item

#lets change the items that are string to lower case

for i,item in enumerate(student_info1):
    if type(item) == str:
        student_info1[i] = item.lower()

print(student_info1)

#just useful in general
#zip()

names = ['juliana','jeremy', 'sonia','john']
cities = ['ramat gan', 'modin', 'ranana', 'tel aviv']

#names_cities = {'juliana':'ramat gan'} ---- we use zip()
# names_cities = zip(names, cities)
# print(names_cities)
# the solution will be <zip object at 0x10f04fc00>

name_cities = dict(zip(names,cities))
print(name_cities)

name_cities = dict(zip(cities,names))
print(name_cities)

