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

def post(request):
    try:
        Token1 = env.ACCESS_TOKEN1
        Token2 = env.ACCESS_TOKEN2
        URL = env.POST_URL
        params = {'evidence': 'Hola prueba2 desde back',
                  'transactionType':'Stamping.io:API'}
        headers = {
                'Authorization': 'Basic {Token1}',
                'Content-Type': 'application/json',
                'Authorization': 'Basic {Token2}'
                }
        response = requests.post(URL,params = params, headers = headers)
        return HttpResponse(response)   
    except Exception as ex:
        return HttpResponse(ex)
    
def get(request):
    try:
        Token = env.ACCESS_TOKEN
        URL = env.GET_URL
        dataTest = "evidence=Hola prueba"
        
        # auth=('Authorization','Basic'+Token)
        headers = {'Authorization': 'basic '+Token}
        response = requests.request("POST",URL+dataTest,headers = headers)
        return HttpResponse(response)   
    except Exception as ex:
        return HttpResponse(ex)
