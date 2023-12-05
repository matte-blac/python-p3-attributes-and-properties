#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name, breed):
# initializes a Dog object with specified name and breed
        self.name = name
        self.breed = breed


    @property
    def name(self):
# retrieves the name of the dog
        return self.name
    
    @name.setter
    def name(self, value):
# sets the name of the dog
        if not isinstance(value, str) or len(value) < 1 or len(value) > 25:
# validates the condition
            print("Name must be string between 1 and 25 characters.")
            return
        self._name = value

    @property
    def breed(self):
# retrieves the breed of the dog
        return self._breed
    
    @breed.setter
    def breed(self, value):
# sets the breed of the dog
        if value not in APPROVED_BREEDS:
# validates the condition
            print("Breed must be in list of approved breeds.")
            return
        self._breed = value
    pass
