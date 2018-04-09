from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from main.actions import check_if_single_option_CDC, get_branch, generate_output

@login_required
def map_options(request):

    return render(request, "/maps/map_options.html")


@login_required
def single_option_CDC_redirect(request): 
	
	# single_option_CDC_logic(students)          
    if request.method == 'POST':
        form = SingleCDCForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data["Year"]
            sem = form.cleaned_data["Sem"]
    		# context["year"]=year
            # return redirect
            print(year, sem)
        else:
            print("not valid")
    return HttpResponse("WORKS!")

	# return render(request, "maps/single_option_CDC_select_success.html", context)


@login_required
def apply_maps_redirect(modeladmin, request, queryset): 
	
	single_option_CDC_logic(students)          

	return render(request, "maps/single_option_CDC_select_success.html", context)