from django.shortcuts import render, redirect

from django.core.paginator import Paginator
from .models import Song
from django.http import HttpResponse

def listenPageView(request):
    #paginator = Paginator(Song.objects.all(), 1)
    #page_number = request.GET.get('page')
    #page_obj = paginator.get_page(page_number)
    #context={'page_obj' : page_obj}
    
    return render(request,'listen/index.html') #FIX THIS TO USE THE ROUTES???


def addSong(request):
    return HttpResponse("Song has been added")

def addSkipVote(request):
    return HttpResponse("Skip vote has been added")


