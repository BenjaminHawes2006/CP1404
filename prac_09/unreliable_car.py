"""
CP1404 Practical 9
Unreliable car subclass of car
"""
from prac_09.car import Car
from random import randint

class UnreliableCar(Car):
    def __init__(self, reliability = 0.0, **kwargs):
        super().__init__(**kwargs)
        self.reliability = reliability

    def __str__(self):
        return f"name: {self.name}, fuel: {self.fuel}, odometer: {self.odometer}, reliability: {self.reliability}%"

    def drive(self, distance):
        random_number = randint(0, 100)
        if random_number < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self.odometer += distance
        else:
            distance = 0
        return distance