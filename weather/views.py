from django.shortcuts import render
import json
import urllib.request
import requests

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        #res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=8a079c959cbbc0b877f6a2f8edca2015').read()
        response = requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=8a079c959cbbc0b877f6a2f8edca2015')
        json_data = response.json()
        #json_data = json.loads(res)
        data = {
            'country': str(json_data['sys']['country']),
            'coordinate': str(str(json_data['coord']['lon'])+','+str(json_data['coord']['lat'])),
            'temp': str(round((json_data['main']['temp']-273.15),2))+' C',
            'pressure':str(json_data['main']['pressure']),
            'humidity':str(json_data['main']['humidity'])
        }
    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'data':data, 'city':city})
