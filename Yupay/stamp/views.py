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
        Token = env.ACCESS_TOKEN
        URL = env.API_URL
        dataTest = "evidence=Hola prueba"
        
        # auth=('Authorization','Basic'+Token)
        headers = {'Authorization': 'basic '+Token}
        request = requests.post(URL+dataTest,headers = headers)
        return HttpResponse(request)   
    except Exception as ex:
        return HttpResponse(ex)
