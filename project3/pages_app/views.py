from django.shortcuts import render 
from django.http import Http404
database = [
    {
        'name':'parsa',
        'last name':'nasdf',
        'number':'858585'
    },
    {
        'name':'mansour',
        'last name':'marasdf',
        'number':'mansoooooooooooorrrrrrrrr zaneto gaiidammmmmmmm'
    },
        {
        'name':'amir',
        'last name':'shir',
        'number':'234567890'
    },
    {
        'name':'alireza',
        'last name':'asdf',
        'number':'8596324862148562'
    }
    
]
# Create your views here.

def base_page(request):
    return render(request, "pages_app/base.html")
def home_page(request, name):
    for person in database:
        if name == person['name']:
            return render(request, "pages_app/home.html", context={'name': person['name'],'number': person['number']}) #address 
    raise Http404("user does not exist")
def users(request):
    return render(request,'pages_app/users.html', context={'database': database})