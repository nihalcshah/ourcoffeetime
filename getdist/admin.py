from django.contrib import admin
from .models import TestResults, TypesOfPlaces, Question, SearchServices
# Register your models here.
admin.site.register(TestResults)
admin.site.register(Question)
admin.site.register(TypesOfPlaces)
admin.site.register(SearchServices)