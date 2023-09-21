from django.shortcuts import render 
import requests
def index(request):

    appid = '1f6e5b9e07e099fd05e3743c51f1470a'
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    param= {'q':'dhaka', 'appid': appid, 'units':'metric'}
    r= requests.get(url=URL,params=param)
    
    res=r.json()
    return render(request,'weatherapp/index.html')