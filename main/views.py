from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST['city']
        source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?q='+ city +'&units=metric&APPID=2231511009911a492018600c5fb2f777').read() 
        
        list_of_data = json.loads(source) 
        data = { 
            "city": city, 
            
            "temp": str(list_of_data['main']['temp']) + '°C', 
            'description' : str(list_of_data['weather'][0]['description']),
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        } 
        print(data) 
    else: 
        data ={} 
    return render(request, "main/index.html", data)
  

