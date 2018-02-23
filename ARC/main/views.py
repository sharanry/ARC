from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def map_options(request):

    return render(request, "/maps/map_options.html")
