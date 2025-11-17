from day2_exersisesxp import Dog #import the dog class
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


