# Exercise 1: Cats
#Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.

class Cat():
    def __init__(self, name, age):
        self.name = name
        self.age = age
      
#cat objects
cat1 = Cat('Mishmish', 12)
cat2 = Cat('Kitty', 4)
cat3 = Cat('Felix', 7)
cat_list = [cat1, cat2, cat3] #created a list to have a key and a value for the function

#function to find the oldest cat:
def find_oldest(cats):
    return max(cats, key=lambda cat: cat.age)

#get the oldest cat:
oldest = find_oldest(cat_list)

# Print the result
print(f"The oldest cat is {oldest.name} and it is {oldest.age} years old.")

print('')
print('--------')
print('')

#Exercise 2 : Dogs
# Create a Dog class, instantiate objects, call methods, and compare dog sizes

#Step 1: Create the Dog Class
class Dog():
    def __init__(self, name, height):#using name and height as parameter
        self.name = name
        self.height = height

    def bark(self):
        print(f"{self.name} barks woof woof")

    def jump(self,):
        x = self.height *2
        print(f'{self.name} jumps {x} cm high!') #where x is height * 2.
              
#Step 2: Create Dog Objects
davids_dog = Dog('Toby', 134)
sarahs_dog = Dog('Luna', 80)

#Step 3: Print Dog Details and Call Methods
print(davids_dog.name, davids_dog.height)
print(sarahs_dog.name, sarahs_dog.height)
davids_dog.bark()
davids_dog.jump()
sarahs_dog.bark()
sarahs_dog.jump()

print('')
print('--------')
print('')

#Exercise 3 : Who’s the song producer?
#Create a Song class with a method to print song lyrics line by line.

class Song():
    def __init__(self, lyrics=[]):
        self.lyrics = lyrics
        

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])

stairway.sing_me_a_song()

print('')
print('--------')
print('')

# Exercise 4 : Afternoon at the Zoo
#Create a Zoo class to manage animals. The class should allow adding animals, 
# displaying them, selling them, and organizing them into alphabetical groups.

#Step 1: Define the Zoo Class
class Zoo():
    def __init__(self,zoo_name): #init with paramete
        self.zoo_name = zoo_name
        self.animals = [] #empty list
        pass

#method adding a new animal where if it is already on the list, it wont add
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f'{new_animal} was added to the zoo.')
            print(self.animals)
        else:
            print(f'{new_animal} is already inside the zoo.')
    

#method to get all animals that are currently in the zoo. if the list is empty, it will show that there are no animals
    def get_animals(self):
        if not self.animals:
            print(f'The {self.zoo_name} Zoo has no animals.')
        else:
            print(', '.join(self.animals))

#method to sell an animal and remove it from the list
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold) #this will remove the sold animal from the list
            print(f'{animal_sold} has been sold')
            print(self.animals)
        else:
            print(f'{animal_sold} was not found in zoo')

#method to sort animals
    def sort_animals(self):
        self.animals.sort() #this sorts the animals alphabetically
        grouped_animals = {} #this creates the dictionary
        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter not in grouped_animals:
                grouped_animals[first_letter] = []
            grouped_animals[first_letter].append(animal)
        
        return grouped_animals

    def get_groups(self):
        print("Grouped Animals:")
        print(self.sort_animals())

#creating the Zoo object
brooklyn_safari = Zoo("Brooklyn Safari")

#use the Zoo methods
print(f'Welcome to {brooklyn_safari.zoo_name} Zoo')
print('')
brooklyn_safari.add_animal("Giraffe")
brooklyn_safari.add_animal("Bear")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Baboon")
brooklyn_safari.add_animal("Goat")
brooklyn_safari.add_animal("Boa")
brooklyn_safari.add_animal("Donkey")
brooklyn_safari.get_animals()
brooklyn_safari.sell_animal("Bear")
brooklyn_safari.sell_animal("Alligator")
print('--------')
print('')
brooklyn_safari.get_animals()
print('--------')
print('')
brooklyn_safari.sort_animals() #this will not show since it has return on the method
print('--------')
print('')
brooklyn_safari.get_groups()
print('--------')
print('')


