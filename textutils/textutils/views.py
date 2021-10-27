#       I have created this file ------ Anurag Srivastava
from django.http import HttpResponse
# Code for Personal Navigator
# def index(request):
#     a = ['''<a href = " https://www.hackerrank.com/anuragsrivasta13 " > Hackerrank Profile</a>''','''\n <a href = " https://www.linkedin.com/in/anurag-srivastava-developer/ " > LinkedIn Profile</a>''','''\n <a href = " https://www.youtube.com/c/Excalibur6969 " > My Youtube Channel</a>''']
#     return HttpResponse(a)
#
# def about(request):
#     return HttpResponse("<h1>About Anurag</h1>")
def index(request):
    return HttpResponse("Home")

def removepunc(request):
    return HttpResponse("remove Punc")

def capfirst(request):
    return HttpResponse("Captitalize First")

def newlineremove(request):
    return HttpResponse("newlineremove")


def spaceremover(request):
    return HttpResponse("Space Remover <a href = '/'> Back  </a>")

def charcount(request):
    return HttpResponse("Character Counter")