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
            
        
    def get(self, request,*args, **kwargs):
        try:
            URL = env.GET_URL
            params = {'byTrxid': '722103692035932df24e5fe43a4fe81c01534e9d'}
            # params = {'byHash': 'insert hash here'}
            response = requests.post(URL,params = params)
            return HttpResponse(response.content)   
        except Exception as ex:
            return HttpResponse(ex)
