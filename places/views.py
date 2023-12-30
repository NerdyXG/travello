from django.shortcuts import render
from .models import Destination
# from django.http import HttpResponse
# Create your views here.

def index(request):

    destination_1 = Destination(
        id = 1,
        image = "destination_1.jpg",
        name = "Bali",
        description = "Bali is a tropical paradise island in Indonesia known for its stunning beaches, rich cultural heritage, vibrant arts scene, and lush landscapes.",
        price = 700
    )

    destination_2 = Destination(
        id = 2,
        image = "destination_2.jpg",
        name = "Indonesia",
        description = "Indonesia is a diverse archipelago nation in Southeast Asia, characterized by its vast cultural heritage, extensive tropical landscapes, and being the world's largest island country.",
        price = 679,
        special_offer = True
    )

    destination_3 = Destination(
        id = 3,
        image = "destination_3.jpg",
        name = "San Francisco",
        description = "San Francisco is a iconic city in Northern California, renowned for the Golden Gate Bridge, diverse neighborhoods, and a vibrant tech culture.",
        price = 800
    )

    destination_4 = Destination(
        id = 4,
        image = "destination_4.jpg",
        name = "Paris",
        description = "Paris, the capital of France, is renowned for its iconic landmarks, exquisite art and architecture, and romantic ambiance.",
        price = 750
    )

    destination_5 = Destination(
        id = 5,
        image = "destination_5.jpg",
        name = "Phi Phi Island",
        description = "Phi Phi Island is a picturesque tropical destination in Thailand, famous for its turquoise waters, limestone cliffs, and vibrant nightlife.",
        price = 600,
        special_offer = True
    )

    destination_6 = Destination(
        id = 6,
        image = "destination_6.jpg",
        name = "Mykonos",
        description = "Mykonos is a picturesque Greek island renowned for its vibrant nightlife, pristine beaches, and charming Cycladic architecture.",
        price = 700
    )

    destinations = [
        destination_1,
        destination_2,
        destination_3,
        destination_4,
        destination_5,
        destination_6
    ]

    return render(request, "index.html", {"destinations": destinations})