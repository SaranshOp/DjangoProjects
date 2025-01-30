from django.http import HttpResponse
from django.shortcuts import render


def home(requests):
    #return HttpResponse("Hello, World! Saransh here.")

    return render(requests, 'websites\index.html', {'name':'index'})



def about(requests):
    return HttpResponse("I am Saransh, a student of Computer Science and Engineering at IIT Roorkee.")

def contact(requests):
    return HttpResponse("You can contact me at  <a href='mailto:    >")
