from django.shortcuts import render, HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from .smileProducer import callProducer

@csrf_exempt
def produceMessage(request):
    if request.method=="POST":
        data = json.loads(request.body)
        callProducer(data)
        return HttpResponse(json.dumps({'status':200,'message': "message send successfully!"}), content_type='application/json')
    return HttpResponse(json.dumps({'status':400,'error': "error"}), content_type='application/json')
