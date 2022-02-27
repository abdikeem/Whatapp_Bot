from django.shortcuts import render
import os
from django.http import HttpResponse
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt

# Create your views here. 
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC42364285298c523c97e02ec136c7d5dc'
auth_token = 'e0b8767477c99749954158e641ae9a3f'
client = Client(account_sid, auth_token)

@csrf_exempt
def bot(request):
    message = request.POST.get('Body')
    sender_name = request.POST.get('ProfileName')
    sender_number = request.POST.get('From')
    print(f"sender:{sender_name} and the message is {message}")

    if message == "hi":
        client.messages.create(
            from_='whatsapp:+14155238886',
            body=f'Hello, {sender_name}, how is it going',
            to='whatsapp:+254721938869'
        )
    return HttpResponse("Hello")
