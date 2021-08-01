from django.shortcuts import render, redirect, get_object_or_404
from getdist.models import TestResults, TypesOfPlaces, Question, SearchServices
import requests, json
from django.db import IntegrityError
from .trial import findList
# Create your views here.

def home_view(request):
    # context = {}
    # results = None
    # results = TestResults.objects.all
    # if results:
    #     context = {'results':results}
    # else:
    #     context = {'results':'Not Found'
    return render(request, "home.html", context = {
        
    })



def collect_view(request):
    if request.method == 'POST':
        
        q = get_object_or_404(Question)
        types = TypesOfPlaces.objects.all()
        selection = request.POST.get(q.question)
        # selection = request.POST.getlist(q.question)
        location = request.POST.get('textfield', None)
        print(location)
        print(selection)
        search = get_object_or_404(SearchServices)
        # string = ""
        # if len(selection)>=1:
        #     for s in selection:
        #         string += s + " "
        try:
            search.location = location
            search.places = selection
            search.save()
        except IntegrityError:
            search.location = "_"
            search.places = "_"
            search.save()
        # search.places = string[:-1]
        location = ""
        selection = ""
        
        return render(request, "collect.html", context = {
            'question':q, 
            'types': types,
        })
    else:
        q = get_object_or_404(Question)
        search = get_object_or_404(SearchServices)
        search.location = "_"
        search.places = "_"
        search.save()
        return render(request, "collect.html", context = {
            'question':q, 
            'types': q.ty.all,
        })
def about_view(request):
    return render(request, "about.html")


def results_view(request):
    if request.method == 'POST':
        
        
        search = get_object_or_404(SearchServices)
        
        # selection = request.POST.getlist(q.question)
        location = search.location
        selection = request.POST.get('categories')
        print(location)
        print(selection)
        results = findList(location, selection)
        name = results['name']
        maps = "https://www.google.com/maps/search/"+name
        imageurl = results['imageurl']
        url = results['url']
        address = results['address']
        phone = results['phone']
        rating = results['rating']
        types = results['type']
        if 'price' in results.keys():
            price = results['price']
            return render(request, "results.html", context = {
                'name' : name,
                'imageurl' : imageurl,
                'url' : url,
                'results': True,
                'address' : address,
                'mapsurl': maps,
                'phone' : phone,
                'rating' : rating,
                'price' : price,
                'types' : types,
            })
        else:
            return render(request, "results.html", context = {
                'name' : name,
                'imageurl' : imageurl,
                'url' : url,
                'address' : address,
                'results': True,
                'mapsurl': maps,
                'phone' : phone,
                'rating' : rating,
                'price' : "Inexpensive",
                'types' : types,
            })
    else:
        search = get_object_or_404(SearchServices)
        location=search.location
        selection =  search.places
        if location == "_" or selection=="_":
            return render(request, "results.html", context = {
                    'results': False,
                })
        else:
            results = findList(location, selection)
            
            name = results['name']
            maps = "https://www.google.com/maps/search/"+name
            imageurl = results['imageurl']
            url = results['url']
            address = results['address']
            phone = results['phone']
            rating = results['rating']
            types = results['type']
            if 'price' in results.keys():
                price = results['price']
                return render(request, "results.html", context = {
                    'name' : name,
                    'imageurl' : imageurl,
                    'url' : url,
                    'results': True,
                    'address' : address,
                    'mapsurl': maps,
                    'phone' : phone,
                    'rating' : rating,
                    'price' : price,
                    'types' : types,
                })
            else:
                return render(request, "results.html", context = {
                    'name' : name,
                    'imageurl' : imageurl,
                    'url' : url,
                    'address' : address,
                    'results': True,
                    'mapsurl': maps,
                    'phone' : phone,
                    'rating' : rating,
                    'price' : "Inexpensive",
                    'types' : types,
                })

    
