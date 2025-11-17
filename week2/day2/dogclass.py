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
    
dog1 = Dog('Rocky', 9 , 149)
dog2 = Dog('Apollo', 11, 154)
dog3 = Dog('Drago', 7, 162)

print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog3))

