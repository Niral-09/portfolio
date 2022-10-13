from multiprocessing import context
from django.shortcuts import render
from .models import Home,About,Portfolio,Profile,Category,Skills
from django.shortcuts import render
def greet(request):
        return render(request,'greet.html')


def index(request):
    home = Home.objects.latest('updated')

    about = About.objects.latest('updated')
    profile = Profile.objects.filter(about = about) 

    categories = Category.objects.all()
    skills = Skills.objects.all()

    portfolios = Portfolio.objects.all()
    

    context = {
        'home':home,
        'about':about,
        'skills':skills,
        'profile':profile,
        'categories':categories,
        'portfolios':portfolios
    }


    return render(request,'index.html',context)

    
