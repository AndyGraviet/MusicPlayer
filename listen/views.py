from django.shortcuts import render
from django.http import HttpResponse

def listen(request):
    return HttpResponse("This will be the listening page")

def addSong(request):
    return HttpResponse("Song has been added")

def addSkipVote(request):
    return HttpResponse("Skip vote has been added")