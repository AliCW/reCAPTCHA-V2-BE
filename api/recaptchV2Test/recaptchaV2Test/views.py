from django.shortcuts import render

from django.http import HttpResponse
from .models import SendKey
import requests
from django.views.decorators.csrf import csrf_exempt

class ReCaptchaV2:
    @csrf_exempt
    def check(request):
        key = SendKey.objects.all()
        checkCAPTCHA = requests.post('https://www.google.com/recaptcha/api/siteverify', data={'secret': key, 'response': request})
        return HttpResponse(checkCAPTCHA)



