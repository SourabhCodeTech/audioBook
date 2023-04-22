from django.shortcuts import render
from .models import Audio, AudioBookName

# Create your views here.
def home(request):
    audioBookName = AudioBookName.objects.all()
    return render(request, 'home.html', {'booksName': audioBookName})

def audiobook(request, str):
    audio = Audio.objects.filter(bookName=str)
    return render(request, 'showAll.html', {'audio': audio})
