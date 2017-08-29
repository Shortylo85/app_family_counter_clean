import json

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import logout
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from ui.forms import RegistrationForm
from ui.models import City, UserCity


# Create your views here.
def index(request):
    
    built_context ={ 'user': request.user }
    return render(request, template_name = "ui/index.html", context = built_context)

def getMap(request):
    
    cities = City.objects.filter(city_name = 'New York')
#     
#     print(cities.city_name)
    
    built_context = {
        'cities': cities,
    }
    
    return render(request, template_name = 'ui/map.html', context = built_context)

def register(request):
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            user = User.objects.last()
            login(request, user)
            if user.is_authenticated():
                us = UserCity(user=user)
                us.save()
                print(us.user.id)

            return redirect('index')
    else:
        form = RegistrationForm()
         
    args = {'form':form}        
     
    return render(request, template_name = 'account/register.html', context = args)

def user_logout(request):
    logout(request)
    
    return redirect('index')
    
def getTerm(request):
    if request.is_ajax():
        search_term = request.GET.get('term','')
        cities = City.objects.filter(city_name__icontains = search_term)[:20]

        result = []
        for city in cities:
            city_json = {}
            city_json['city_name'] = city.city_name
            
            result.append(city_json)
        data = json.dumps(result)
        print('this is results\n',result)
        print("THIS IS CITIES ---------> ", data)
    else:
        data = 'fail'
    mimetype = 'application/json'
    
    return HttpResponse(data, mimetype)

def saveLocation(request):
     
    if request.method == 'POST':
        return HttpResponse(request.method)

        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 
        
        
        
        
        
        