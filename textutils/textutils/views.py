#       I have created this file ------ Anurag Srivastava
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello Anurag</h1>")

def about(request):
    return HttpResponse("<h1>About Anurag</h1>")