#Daily challenge: Old MacDonald’s Farm
#You are given example code and output. Your task is to create a Farm class that produces the same output.

class Farm():
    def __init__(self, name): #created the _init_ method with one parameter
        self.name = name
        self.animals = {}
        #created two atributes inside the init method
        
#method to add animals
    def add_animal(self, animal_type, count = 1):
        
        if animal_type in self.animals: #this is to add 1 count if the animals already exists
            self.animals[animal_type] += count
            print(self.animals)
            
        else:
            self.animals[animal_type] = count
            print(f'{animal_type} was added to the farm.')  
            print(self.animals)
    
#get info method
    def get_info(self):
        print(f"Farm Name: {self.name}")
        print("Animals:")
        for animal, count in self.animals.items():# this will show the animal dictionary in each row
            print(f"  {animal}: {count}")
        print("E I E I O")

   
#Bonnus
#get_animal_types
    def get_animal_types(self):
        sorted_animals = sorted(self.animals) #to call the keys in the animal dict from a-z
        return sorted_animals

#Implement the get_short_info Method
    def get_short_info(self):
        animals_list = []
        for animal,count in self.animals.items():
            if count > 1:
                animals_list.append(animal + "s")
            else:
                animals_list.append(animal)
        animals_str = ", ".join(animals_list)
        print(f"{self.name}'s farm has {animals_str}.")


    

farm1 = Farm("MacDonald")
farm1.add_animal('cow', 5)
farm1.add_animal('sheep')
farm1.add_animal('sheep')
farm1.add_animal('zebra')
farm1.add_animal('goat', 12)
farm1.add_animal('goat', 12)
print('-----------')
# farm1.get_info()
print(farm1.get_animal_types())
farm1.get_short_info()

