from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<body style="background-color:powderblue;"><center><h1>I am up and running!!!!!</h1></body>')


def tests(request):
    return render(request, 'rskgame/tests.html')
