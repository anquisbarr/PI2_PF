from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import HttpRequest
from Yupay import environment as env
from django.template import loader
import requests
from django.http import JsonResponse
from django.views import View
from hashlib import sha256
import base64
from .models import Person
# Create your views here. 
# All the views must be called in the urls



def index(request): #after request you may include other parameters
    # template = loader.get_template('root/file.html')
    try:
        return render(request,'index.html')
    except Exception as ex:
        return HttpResponse(ex)

def forms(request): 
    try:
        return render(request,'forms.html')
    except Exception as ex:
        return HttpResponse(ex)
    
def searchForm(request): 
    try:
        return render(request,'search.html')
    except Exception as ex:
        return HttpResponse(ex)
    
def search(request,id):
    try:
        URL = env.GET_URL
        #data = json.loads(request.body)
        #DNI = data['user_id']
        DNI = id
        response = None
        try:
            instance = Person.objects.get(DNI=str(DNI))
            reference = instance.base_trxid
            params = {'byTrxid': str(DNI)}
            response = requests.get(URL,params = params)
        except Exception:
            response = {'respuesta':"EL DNI NO SE HA REGISTRADO"}
            response = json.dumps(response)
        # params = {'byHash': 'insert hash here'}
        print(json.loads(response))
        return HttpResponse(response.body)
    except Exception as ex:
        print(ex)
        return HttpResponse(ex)
    
def search2(request):
    try:
        URL = env.GET_URL
        #data = json.loads(request.body)
        #DNI = data['user_id']
        DNI = id
        response = None
        try:
            instance = Person.objects.get(DNI=str(DNI))
            reference = instance.base_trxid
            params = {'byTrxid': str(DNI)}
            response = requests.get(URL,params = params)
        except Exception:
            response = {'respuesta':"EL DNI NO SE HA REGISTRADO"}
            response = json.dumps(response)
        # params = {'byHash': 'insert hash here'}
        print(json.loads(response))
        return HttpResponse(response.body)
    except Exception as ex:
        print(ex)
        return HttpResponse(ex)


        
class stamping(View):
    def post(self,request,*args, **kwargs):  
        if request.method == "POST":      
            try: 
                Token = env.ACCESS_TOKEN
                URL = env.POST_URL
                data = json.loads(request.body)
                reference = None
                response = None
                headers = {
                            'Authorization': f'Basic {Token}',
                            'Content-Type': 'application/json'}
                dni = data['user_id']
                try:
                    instance = Person.objects.get(DNI=dni)
                    reference = instance.base_trxid
                    h = sha256(json.dumps(data).encode('utf-8'))
                    params = {"evidence": h.hexdigest(),
                        'transactionType':'Stamping.io:API',
                            'data': base64.b64encode(json.dumps(data).encode('utf-8')),
                            'subject':'Added Data',
                            'reference':reference}
                    response = requests.post(URL,params = params, headers = headers)
                except Exception as ex:
                    h = sha256(json.dumps(data).encode('utf-8'))
                    params = {"evidence": h.hexdigest(),
                            'transactionType':'Stamping.io:API',
                                'data': base64.b64encode(json.dumps(data).encode('utf-8')),
                                'subject':'newUser'}
                    
                    response = requests.post(URL,params = params, headers = headers)
                    newRow = Person(data['user_id'],json.loads(response.content)['trxid'])
                    newRow.save()
                return HttpResponse(response.content)  
            except Exception as ex:
                print(ex)
                return HttpResponse("error: "+str(ex))
            
