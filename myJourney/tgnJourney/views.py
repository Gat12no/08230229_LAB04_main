from django.shortcuts import render
from .models import LearningJourney, AboutMe
# Create your views here.


def index(request):
    journeys = LearningJourney.objects.all()
    return render(request, 'tgnJourney/index.html', {'journeys': journeys})

def about_me(request):
    abouts = AboutMe.objects.all()
    return render(request, 'tgnJourney/aboutMe.html', {'abouts': abouts})

def index(request):
    return render(request, 'tgnJourney/index.html')