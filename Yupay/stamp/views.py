from django.shortcuts import render
from django.http import HttpResponse
import json.encoder
from django.http import HttpRequest
from Yupay import environment as env
import requests 
# Create your views here. 
# All the views must be called in the urls
def index(request): #after request you may include other parameters
    # template = loader.get_template('root/file.html')
    response = "Hello, world. You're at the polls index."
    #return HttpResponse(template.render(response,request))
    return HttpResponse(response)

def stamp(request):
    Token = env.ACCESS_TOKEN
    URL = env.API_URL
    data = {"evidence":"Hash-256 (Input)","transactionType":"Stamping.io:API"}
    dataTest = "hola"
    request = requests.get(URL + dataTest, auth=('Authorization', 'basic '+ Token))
    #HttpRequest.POST(json.JSONEncoder(data))
    return HttpResponse(data)   