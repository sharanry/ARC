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
        print("YES IT REACHED")
        form = MapsForm(request.POST)
        # myForm.cleaned_data.get('description')
        # print(form.cleaned_data["students"])
        # return HttpResponse(form.cleaned_data.get('students'))
        if form.is_valid():
            maps = form.cleaned_data["Course_Map"]
            students = form.cleaned_data["students"]

            # Apply logic

            # return HttpResponse(form.cleaned_data["students"])
            # print(maps, students)
            # print(RequestContext(request))
        else:
            print("not valid")
        
            return HttpResponse(":(")    
    return HttpResponse("WORKS!")

    return render(request, "/maps/map_options.html")


@login_required
def single_option_CDC_redirect(request):           
    if request.method == 'POST':
        form = SingleCDCForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data["Year"]
            sem = form.cleaned_data["Sem"]
            students=form.cleaned_data["students"]
            # print(year, " ", sem, " ", students[0] )
            single_option_CDC_logic(students, year, sem)
                #  return HttpResponse("IF LOOP")

            # context["year"]=year
            # return redirect
            # print(year, sem)
        else:
            print("not valid")
    return HttpResponse("Outputs Generated Successfully!")

    # return render(request, "maps/single_option_CDC_select_success.html", context)


# @login_required
# def apply_maps_redirect(modeladmin, request, queryset): 
    
#     single_option_CDC_logic(students)          

#     return render(request, "maps/single_option_CDC_select_success.html", context)