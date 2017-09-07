import json
from json.encoder import JSONEncoder

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.views import logout
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, render_to_response

from ui.forms import RegistrationForm, FamilyForm
from ui.models import City, UserCity, Chat


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

def getMap1(request):
    return render(request, template_name= 'ui/map1.html')

def register(request):
    
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid:
            form.save()
            user = User.objects.last()
            login(request, user)
#             if user.is_authenticated():
#                 us = UserCity(user=user)
#                 us.save()
#                 print(us.user.id)

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
            city_json = city.city_name 
        
            
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
        city_picked = request.POST.get('search_term')
        print("This is city from search input --> {}".format(city_picked))
        city = City.objects.filter(city_name = city_picked).get()
        user = request.user
        u_s = UserCity(user=user,city=city)
        u_s.save()

        user_city_all = UserCity.objects.all()
        
        lista=[]
        
        for item in user_city_all:
            json_1 = {}
            json_1["lat"] = float(item.city.lat)
            json_1["lng"] = float(item.city.lng)
            lista.append(json_1)
        
        print('____THIS IS LISTA_____',lista)

        data = json.dumps(lista)

        print('____THIS IS data_____',data)
        
            

        built_context={
            'u_s': u_s,
            'user_city_all': user_city_all,
            'json_list': data,
        }
#         print(built_context)
#         return render(request, template_name = 'ui/map.html', context = built_context)
        return render_to_response(template_name ='ui/map.html',context = built_context)

def saveLocation1(request):
    
    if request.method == 'POST':
        
        place = request.POST.get("pac-input")
        lat = request.POST.get("lat")
        lng = request.POST.get("lng")

        city = City(city_name = place, lat = lat, lng = lng)
        city.save()
        
#         u_c = UserCity(user = request.user, city = city)
# 
#         u_c.save()

        u_c, created = UserCity.objects.update_or_create(
            user = request.user, 
            defaults = {'user': request.user,
                       'city': city 
            }
        )
        u_c.save()

        user_city_all = UserCity.objects.all()
            
        lista=[]
             
        for item in user_city_all:
            json_1 = {}
            json_1["lat"] = float(item.city.lat)
            json_1["lng"] = float(item.city.lng)
            lista.append(json_1)

        data = json.dumps(lista)

        built_context={
            'u_c': u_c,
            'user_city_all': user_city_all,
            'json_list': data,
        }

        return render(request, template_name = 'ui/map.html', context = built_context)
#         return render_to_response(template_name ='ui/map.html',context = built_context)

        
def chat(request):
    
    chats = Chat.objects.all()
    built_context = {'chats': chats}
    
    return render(request, template_name = 'ui/chat.html', context = built_context)

def postMessage(request):
    
    if request.method == 'POST':
        msg = request.POST.get('msg_value', None)
        print(msg)
        chat_s = Chat(user=request.user, message=msg)
        if msg != '':
            chat_s.save()
        return JsonResponse({'msg':msg, 'user':chat_s.user.username})
    else:
        return HttpResponse("Response must be method = POST")

def getMessage(request):
    
    chats = Chat.objects.all()
    built_context = {'chats': chats}
    
    return render(request, template_name = 'ui/messages.html', context = built_context)
        
def showTree(request):
    return render(request, template_name = 'ui/tree.html')      



def getFamilyForm(request):
    family_form = FamilyForm()
    
    built_context = {'family_form': family_form}
    
    return render(request, template_name='ui/family_form.html', context = built_context)  
    

def postFamilyForm(request):

    family_form = FamilyForm(request.POST)
    if family_form.is_valid():
        
        otac = family_form.cleaned_data['otac']
        majka = family_form.cleaned_data['majka']
        oceva_majka = family_form.cleaned_data['oceva_majka']
        ocev_otac = family_form.cleaned_data['ocev_otac']
        majcina_majka = family_form.cleaned_data['majcina_majka']
        majcin_otac = family_form.cleaned_data['majcin_otac']
        oceva_baba_po_ocu = family_form.cleaned_data['oceva_baba_po_ocu']
        ocev_deda_po_ocu = family_form.cleaned_data['ocev_deda_po_ocu']
        majcina_baba_po_ocu = family_form.cleaned_data['majcina_baba_po_ocu']
        majcin_deda_po_ocu = family_form.cleaned_data['majcin_deda_po_ocu']
        oceva_baba_po_majci = family_form.cleaned_data['oceva_baba_po_majci']
        ocev_deda_po_majci = family_form.cleaned_data['ocev_deda_po_majci']
        majcina_baba_po_majci = family_form.cleaned_data['majcina_baba_po_majci']
        majcin_deda_po_majci = family_form.cleaned_data['majcin_deda_po_majci']
        
        lista = []
        json1 = {}
        json1 = {
            'user': request.user.username,
            'otac': otac,
            'majka': majka,
            'oceva_majka': oceva_majka,
            'ocev_otac': ocev_otac,
            'majcina_majka': majcina_majka,
            'majcin_otac': majcin_otac,
            'oceva_baba_po_ocu': oceva_baba_po_ocu,
            'ocev_deda_po_ocu': ocev_deda_po_ocu,
            'majcina_baba_po_ocu': majcina_baba_po_ocu,
            'majcin_deda_po_ocu': majcin_deda_po_ocu,
            'oceva_baba_po_majci': oceva_baba_po_majci,
            'ocev_deda_po_majci': ocev_deda_po_majci,
            'majcina_baba_po_majci': majcina_baba_po_majci,
            'majcin_deda_po_majci': majcin_deda_po_majci,   
        }
        lista.append(json1)
        
        data = json.dumps(lista)
        
        built_context = {
            'data': data,
        }

    
    return render(request, template_name='ui/tree.html', context = built_context)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 
        
        
        
        
        
        