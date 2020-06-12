from django.shortcuts import render
from django.http import HttpResponse
import json.encoder
from django.http import HttpRequest
from Yupay import environment as env
# Create your views here. 
# All the views must be called in the urls
def index(request): #after request you may include other parameters
    # template = loader.get_template('root/file.html')
    response = "Hello, world. You're at the polls index."
    #return HttpResponse(template.render(response,request))
    return HttpResponse(response)

def stamp(request):
    if request == "POST":
        try:
            Token = env.ACCESS_TOKEN
            URL = env.API_URL
            dataTest = "hola"
            #request = requests.post(URL,headers,)
            #HttpRequest.POST(json.JSONEncoder(data))
            return HttpResponse(dataTest)   
        except Exception as ex:
            return HttpResponse(ex)