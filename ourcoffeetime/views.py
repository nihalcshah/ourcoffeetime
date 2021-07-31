from django.shortcuts import render, redirect, get_object_or_404
from getdist.models import TestResults, TypesOfPlaces, Question
# Create your views here.

def home_view(request):
    # context = {}
    # results = None
    # results = TestResults.objects.all
    # if results:
    #     context = {'results':results}
    # else:
    #     context = {'results':'Not Found'}
    return render(request, "home.html", context = {
        
    })

def results_view(request):
    result = get_object_or_404(TestResults)
    return render(request, "results.html", context = {
        'results':result
    })

def collect_view(request):

    q = get_object_or_404(Question)
    return render(request, "collect.html", context = {
        'question':q, 
        'types': q.ty.all,
    })

def about_view(request):
    return render(request, "about.html")


    
