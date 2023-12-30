from django.db import models

# Create your models here.

class Destination:
    def __init__(self, id, image="Image N/A", name="Name N/A", description="Description N/A", price="Price N/A", special_offer = False):
        self.id = id
        self.image = image
        self.name = name
        self.description = description
        self.price = price
        self.special_offer = special_offer

    # id: int
    # name: str
    # description: str
    # price: int