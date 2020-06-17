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
        inputPrueba = {'Id': '124124124'}
        Token = env.ACCESS_TOKEN
        URL = env.POST_URL
        data = {'Id': '124124124',
                'compra' : 'producto1',
                'valor': 300
        }
        summary = json.dumps(dict(inputPrueba, **data))
        h = sha256(summary.encode('utf-8'))
        params = {'evidence': h.hexdigest(),
                  'transactionType':'Stamping.io:API',
                    'data': json.dumps(data)}
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
