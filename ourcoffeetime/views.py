from django.shortcuts import render, redirect, get_object_or_404
from getdist.models import TestResults
# Create your views here.

def home_view(request):
    # context = {}
    # results = None
    # results = TestResults.objects.all
    # if results:
    #     context = {'results':results}
    # else:
    #     context = {'results':'Not Found'}
    result = get_object_or_404(TestResults)
    return render(request, "home.html", context = {
        'results':result
    })

def results_view(request):
    return render(request, "results.html")
