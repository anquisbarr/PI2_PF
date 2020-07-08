from django.shortcuts import render
from django.http import HttpResponse
import json
from django.http import HttpRequest
from Yupay import environment as env
from django.template import loader
from django.template.loader import render_to_string
from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views import View
from hashlib import sha256
from django.views.decorators.csrf import csrf_exempt
import base64
# Create your views here. 
# All the views must be called in the urls
def index(request): #after request you may include other parameters
    # template = loader.get_template('root/file.html')
    try:
        #return HttpResponse(template.render(response,request))
        return render(request,'index.html')
    except Exception as ex:
        return HttpResponse(ex)
    
def forms(request): 
    try:
        return render(request,'forms.html')
    except Exception as ex:
        return HttpResponse(ex)
    
class stamping(View):
    '''def post(self,request,*args, **kwargs):        
        try: 
            inputPrueba = {'Id': '124124124'}
            Token = env.ACCESS_TOKEN
            URL = env.POST_URL
            data = {'Id': '124124',
                    'compra' : 'producto1',
                    'valor': 300
            }
            summary = json.dumps(dict(inputPrueba, **data))
            h = sha256(summary.encode('utf-8'))
            params = {"evidence": h.hexdigest(),
                    'transactionType':'Stamping.io:API',
                        'data': base64.b64encode(json.dumps(data).encode('utf-8')),
                        'subject':'Asunto'}
            # params lat long(num or string)
            # url 
            #reference = trxid 
            headers = {
                    'Authorization': f'Basic {Token}',
                    'Content-Type': 'application/json'}
            
            response = requests.post(URL,params = params, headers = headers)
            return HttpResponse(response)   
        except Exception as ex:
            print(ex)
            return HttpResponse(ex)'''
            
    def post(self,request):
        if request.method == "POST":
            try: 
                data = json.loads(request.body)
                Token = env.ACCESS_TOKEN
                URL = env.POST_URL
                summary = data
                h = sha256(summary.encode('utf-8'))
                params = {"evidence": h.hexdigest(),
                            'transactionType':'Stamping.io:API',
                            'data': base64.b64encode(json.dumps(data).encode('utf-8')),
                            'subject':'Asignacion'}
                headers = {
                    'Authorization': f'Basic {Token}',
                    'Content-Type': 'application/json'}
                
                response = requests.post(URL,params = params, headers = headers)
                return HttpResponse(data) 
            except Exception as ex:
                return HttpResponse(ex)
        
    def get(self, request,*args, **kwargs):
        try:
            URL = env.GET_URL
            params = {'byTrxid': '95f1165e976b1dfe14486a167a6b28b7e3444aa3'}
            # params = {'byHash': 'insert hash here'}
            response = requests.post(URL,params = params)
            return HttpResponse(response)   
        except Exception as ex:
            return HttpResponse(ex)
