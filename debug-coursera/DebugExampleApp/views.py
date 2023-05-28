#from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def display_even_numbers(request):
    response = ""
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in numbers:
        remainder = i % 2
    if remainder == 0:
        response += str[i] + "Oh! it works"
    return HttpResponse(response)
