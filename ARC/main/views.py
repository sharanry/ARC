from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from main.forms import *
from main.actions import *
from django.template import RequestContext

@login_required
def map_options(request):
    if request.method == 'POST':
        form = MapsForm(request.POST)
        if form.is_valid():
            maps = form.cleaned_data["Course_Map"]
            students = form.cleaned_data["students"]
            for m in maps:
                print(m.courseSlots)
            for s in students:
                print(s)
            # apply_maps_logic(students, maps)
        else:
            print("not valid")
        
            return HttpResponse(":(")    
    return HttpResponse("Maps Generated Successfully!")


@login_required
def single_option_CDC_redirect(request):           
    if request.method == 'POST':
        form = SingleCDCForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data["Year"]
            sem = form.cleaned_data["Sem"]
            students=form.cleaned_data["students"]
            single_option_CDC_logic(students, year, sem)
        else:
            print("not valid")
    return HttpResponse("CDCs Generated Successfully!")