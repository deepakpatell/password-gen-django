from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/index.html',{'pass':'deepak from dictionary'})

def p1(request):
    character = list('abcdefghijklmnopqrstuvwxyz')
    length= int(request.GET.get('length'))
    if request.GET.get('UPPERCASE'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Digits'):
        character.extend(list('0123456789'))

    if request.GET.get('Special Char'):
        character.extend(list('@#$%&*'))
    genNew=''
    for x in range(length):
        genNew += random.choice(character)
    return render(request,'generator/p1.html',{'pass':genNew})
def about(request):
    return render(request,'about/about.html')
