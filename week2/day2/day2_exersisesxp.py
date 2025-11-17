# Exercise 1: Pets

#Instructions:
# Use the provided Pets and Cat classes to create a Siamese breed, 
# instantiate cat objects, and use the Pets class to manage them.
print('Exercise 1: Pets')
print('')
class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'
    


#Step 1: Create the Siamese class
class Siamese(Cat):
    pass

#Create a List of Cat Instances
bengal_obj = Bengal('Tiger', 5)
chartreux_obj = Chartreux('Pepe', 3)
siamese_obj = Siamese('Mishmish', 7)

#Create a Pets instance of the list of cat instances
all_cats = [bengal_obj, chartreux_obj, siamese_obj]

sara_pets = Pets(all_cats) #instance of the list of cat instances

sara_pets.walk() #Take cats for a walk

print('')
print('------')
# Exercise 2: Dogs
#Create a Dog class with methods for barking, running speed, and fighting.
print('Exercise 2: Dogs')
print('')
#Dog class
class Dog():
    def __init__(self, name, age, weight):
        #coding the attributes
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        # ... code to return bark message ...
        return f'{self.name} is barking.'

    def run_speed(self):
        # ... code to return run speed ...
        return int(self.weight / self.age) * 10

    def fight(self, other_dog):
        self_attack = self.run_speed() * self.weight
        other_dog_attack = other_dog.run_speed() * other_dog.weight
        if self_attack > other_dog_attack:
            return f'The winner is {self.name}'
        elif other_dog_attack > self_attack:
            return f'The winner is {other_dog.name}'
        else:
            return 'Ther is a tie'


#Create Dog Instances with diff names, ages and weights
dog1 = Dog('Rocky', 6 , 155)
dog2 = Dog('Apollo', 8, 158)
dog3 = Dog('Drago', 7, 162)

print(dog1.bark())
print(dog3.bark())
print(dog2.run_speed())
print(dog3.run_speed())
print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog1.fight(dog3))

print('')
print('------')
#Exercise 3: Dogs Domesticated:
#Create a PetDog class that inherits from Dog and adds training and tricksfrom day2_exersisesxp import Dog #import the dog class
import random
class PetDog(Dog):
    def __init__(self, name, age, weight, ): # <mark> no need to put the details in the function, you are giving the solution</mark>
        super().__init__(name, age, weight)
        self.trained = False

    def train(self): 
        print(self.bark())
        self.trained = True

    def play(self, *dog_names):
        all_dog_names = [dog_names]
        for name in dog_names:
            if isinstance(name, str) and name.strip():
                all_dog_names.append(name.strip())

        if len(dog_names) > 1:
            print(f'{', '.join(dog_names)} play together!')
        else:
            print(f'{self.name} plays alone.')
            
        # ... code to print play message ...

    def do_a_trick(self): 
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead", "fetches ball", "sings and dance"]
            print(f"{self.name} {random.choice(tricks)}")



dog_names = ['Rocky', 'Apollo', 'Drago']
my_dog = PetDog("Fido", 2, 10)
my_dog.train()
my_dog.do_a_trick()

my_dog.play('Fido', 'Rocky', 'Apollo', 'Drago',)
print('------')
print('')
#Execise 4:Family and Person Classes
print('Exercise 4: Family and Person Classes')

#Practice working with classes and object interactions by modeling a 
# family and its members

# #Step 1: Create the Person Class first_name age
# last_name (string, should be initialized as an empty string)
class Person():
    def __init__(self, first_name, age, last_name = '' ):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name
#Add a method called is_18():
# It should return True if the person is 18 or older, otherwise False.  
    def is_18(self):
        return self.age >= 18

#Step 2: Create the Family Class
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []
    
    def born(self, first_name, age):
        person = Person(first_name, age, self.last_name)
        self.members.append(person)
        
    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print(f"{first_name}, you are over 18, your parents Carmela and Vito accept that you will go out with your friends")
                else:
                    print(f"Sorry {first_name}, you are not allowed to go out with your friends.")
                return # Exit once the person is found and checked
        print(f"Person with first name {first_name} not found in this family.")

    def family_presentation(self):
        print(f"Family Last Name: {self.last_name}")
        for person in self.members:
            print(f"  - {person.first_name}, Age: {person.age}")

# Create a family
my_family = Family("Corleone")

# Add members to the family using the born() method
my_family.born("Sony", 36)
my_family.born("Fredo", 49)
my_family.born("Connie", 16)
my_family.born("Michael", 22)

# Use check_majority() to see if someone is allowed to go out
print("\nChecking majority status:")
my_family.check_majority("Michael")
my_family.check_majority("Connie")
my_family.check_majority("Sony")
my_family.check_majority("Emilio") # Check for a person not in the family

#  Display family information with family_presentation()
print("\nFamily Presentation:")
my_family.family_presentation()