"""ARC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views, actions
# from main.views import single_option_CDC_redirect


urlpatterns = [
    path('mapsuccess', views.map_options),
    path('', admin.site.urls), 
	path('cdcsuccess', views.single_option_CDC_redirect),

]
# urlpatterns += patterns('myview.views',
#     url(r'^(?P<user>\w+)/', 'myview', name='myurl'), # I can't think of a better name
# )
