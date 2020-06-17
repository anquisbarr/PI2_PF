from django.shortcuts import render
from django.http import HttpResponse
import json.encoder
from django.http import HttpRequest
from Yupay import environment as env
import requests
from hashlib import sha256
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
        URL = env.POST_URL
        data = b"Hola prueba hashing"
        h = sha256(data)
        params = {'evidence': h.hexdigest(),
                  'transactionType':'Stamping.io:API'}
        headers = {
                'Authorization': f'Basic {Token}',
                'Content-Type': 'application/json'}
        
        response = requests.post(URL,params = params, headers = headers)
        return HttpResponse(response)   
    except Exception as ex:
        return HttpResponse(ex)
    
def get(request):
    try:
        URL = env.GET_URL
        params = {'byTrxid': '95f1165e976b1dfe14486a167a6b28b7e3444aa3'}
        # params = {'byHash': 'insert hash here'}
        response = requests.post(URL,params = params)
        return HttpResponse(response)   
    except Exception as ex:
        return HttpResponse(ex)
