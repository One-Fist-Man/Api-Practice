from django.shortcuts import render 
import requests
import datetime
def index(request):

    if 'city' in request.POST:
        city = request.POST['city']
    else :
        city = 'Dhaka'
    print(city)
    appid = '1f6e5b9e07e099fd05e3743c51f1470a'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    param= {'q':city, 'appid': appid, 'units':'metric'}

    r= requests.get(url = URL, params = param)

    res=r.json()

    # print(len(res))
    if len(res)>2:
        description= res['weather'][0]['description']
        icon=res['weather'][0]['icon']
        temp=res['main']['temp']
        day= datetime.date.today()

        return render(request,'weatherapp/index.html',{'description':description,
        'icon':icon,
        'temp':temp,
        'day':day,
        'city':city,
        'error':'0'} )
    else :
        return render(request,'weatherapp/index.html',{'error':'1'} )