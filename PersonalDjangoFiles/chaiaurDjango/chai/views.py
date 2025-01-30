from django.shortcuts import render

# Create your views here.

def all_chai(requests):
    return render(requests, 'chai\\all_chai.html', {'name':'all_chai'})

def order(requests):
    return render(requests, 'chai/order.html', {'name':'order'})