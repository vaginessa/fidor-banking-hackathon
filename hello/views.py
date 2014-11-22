import requests
import json
import time

from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from fidor import FidorClient


access_token = 'bb0c4de1ec6fda142d48991995f0dbaa'
api_url = 'https://aps.fidor.de'

def index(request):
    fidor = FidorClient(access_token, api_url)
    account = fidor.accounts.get(8)
    
    return render(request, 'index.html', {'account': account})

def transfer(request):
    fidor = FidorClient(access_token, api_url)

    #payload = {
    #    'account_id': 8,
    #    'amount': 1,
    #    'external_uid': int(time.time()),
    #    'receiver': '99996807',
    #    'currency': 'EUR',
    #    'subject': 'Tak for kaffe!'
    #}

    payload = {
        'account_id': 8,
        'amount': 1,
        'remote_iban': 'DE04333706726265131076',
        'external_uid': int(time.time()),
        'subject': 'Tak for kaffe!'
    }



    print fidor.sepa_credit_transfers.create(payload)
    account = fidor.accounts.get(8)


    return render(request,'transfer.html', {'account': account})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

