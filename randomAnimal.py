import random

animalTypes = ["Dog", "Cat", "Rabbit", "Bird", "Fish", "Horse", "Snake"]

def randomAnimal():
     age = random.randint(1, 30)
     type = random.choice(animalTypes)
     price = random.randint(100, 7500)
     
     animal = {"age": age, "category": type, "price": price}
     return animal