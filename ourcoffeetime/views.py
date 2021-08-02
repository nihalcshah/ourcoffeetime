from django.shortcuts import render, redirect, get_object_or_404
from getdist.models import TestResults, TypesOfPlaces, Question, SearchServices
import requests, json
from django.db import IntegrityError
from .trial import findList, randomize
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
        
        q = Question.objects.all()
        # p = ""
        for i in q:
            if(i.previous == True):
                p = i
        search = get_object_or_404(SearchServices)
        types = TypesOfPlaces.objects.all()
        selection = request.POST.get('Output')
        keyword = request.POST.get('keyword', default="")
        k = request.POST.get('textfield', None)
        location = None
        if not k==None:
            location = k
        if location:
            print("location " + location)
            search.location = location
            search.save()
        if selection:
            if keyword:
                search.places = keyword
            else:
                search.places = selection
            search.save()
        print(selection)
        print("searches " + search.location)

        if(selection=="Drinks"):
            
            for i in q:
                if(i.style == "drinks"):
                    p = i
                else:
                    i.previous = False
                    i.save()
            p.previous = True
            p.save()
            search = get_object_or_404(SearchServices)
            print(search.location)
            # try:
            search.location = location
            if keyword:
                search.places = keyword
            else:
                search.places = selection
            search.save()
            # except IntegrityError:
            #     search.location = "_"
            #     search.places = "_"
            #     search.save()
            # search.places = string[:-1]
            print(p.question)
            return render(request, "collect.html", context = {
                'question':p, 
                'show':True,
                'types': p.ty.all,
                'loc': False
            })
        
        if(selection=="Food"):
            
            for i in q:
                if(i.style == "food"):
                    p = i
                else:
                    i.previous = False
                    i.save()
            p.previous = True
            p.save()
            search = get_object_or_404(SearchServices)
            try:
                search.location = location
                if keyword:
                    search.places = keyword
                else:
                    search.places = selection
                search.save()
            except IntegrityError:
                search.location = "_"
                search.places = "_"
                search.save()
            # search.places = string[:-1]
            location = ""
            selection = ""
            print(p.question)
            return render(request, "collect.html", context = {
                'question':p, 
                'show':True,
                'types': p.ty.all,
                'loc': False
            })

        # p = ""
        # for i in q:
        #     if(i.style == "_"):
        #         p = i

        print("searches " + search.location)
        location = ""
        selection = ""
        
        return render(request, "collect.html", context = {
            'question':p, 
            'show':False,
            'types': p.ty.all,
            'loc': True
        })
    else:
        q = Question.objects.all()
        search = get_object_or_404(SearchServices)
        search.location = "_"
        search.places = "_"
        search.save()
        p = ""
        for i in q:
            if(i.style == "_"):
                p = i
        return render(request, "collect.html", context = {
            'question':p, 
            'show': True,
            'types': p.ty.all,
            'loc': True
        })
def about_view(request):
    return render(request, "about.html")


def results_view(request):
    if request.method == 'POST':
        
        
        search = get_object_or_404(SearchServices)
        
        # selection = request.POST.getlist(q.question)
        location = search.location
        selection = request.POST.get('categories')
        skip = request.POST.get('try')
        print(location)
        print(selection)
        if selection:
            results = findList(search.location, selection)
        else:
            results = randomize(search.location, search.places)
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
        print("location: "+  search.location)
        print("place: "+ search.places)
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

    
