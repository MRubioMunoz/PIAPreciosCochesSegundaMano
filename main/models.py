from django.db import models

# Create your models here.

class Coche: 
    def __init__(self):
        self.km = 0
        self.fuelTypeId = 0
        self.makeId = 0
        self.modelId = 0
        self.transmissionTypeId = 0
        self.year = 0
        self.cubicCapacity = 0
        self.door = 0
        self.hp = 0


coche = Coche()


