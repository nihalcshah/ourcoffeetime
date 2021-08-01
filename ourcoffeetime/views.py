from django.shortcuts import render, redirect, get_object_or_404
from getdist.models import TestResults, TypesOfPlaces, Question, SearchServices
import requests, json
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
        search.location = location
        search.places = selection
        # search.places = string[:-1]
        location = ""
        selection = ""
        search.save()
        return render(request, "collect.html", context = {
            'question':q, 
            'types': types,
        })
    else:
        q = get_object_or_404(Question)
        return render(request, "collect.html", context = {
            'question':q, 
            'types': q.ty.all,
        })
def about_view(request):
    return render(request, "about.html")


def results_view(request):
    api_key = 'NbEE2licArPR88IEjsCsbm6YhSF4_elK2Wu-StTxq9Ee-UG-C1gxyTiZv7s_g1nxDnSlFxLpeEpfiFX5FTVnwdCFrgH7fwNHP9PG55O5c7Osijhk_zC95ob2Zb8FYXYx'
    search_api_url = 'https://api.yelp.com/v3/businesses/search'
    search = get_object_or_404(SearchServices)
    location=search.location
    selection =  search.places
    if location == "" or selection=="_":
        return render(request, "results.html", context = {
            'results':'There are no results'
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
                'mapsurl': maps,
                'phone' : phone,
                'rating' : rating,
                'price' : "Inexpensive",
                'types' : types,
            })

    
