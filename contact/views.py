# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import Contact, Message



# 联系的页面
def contact_page(request):

    return render(request, 'contact.html')



def contacts(request):

    contact = Contact.objects.all().order_by('?')[0]

    d = {}
    d['location'] = contact.location
    d['location_picture'] = contact.location_picture.url
    d['email'] = contact.email
    d['email_picture'] = contact.email_picture.url
    d['phone'] = contact.phone
    d['phone_picture'] = contact.phone_picture.url

    data = json.dumps(d)

    return HttpResponse(data, content_type='application/json')


def message(request):

    if request.method == 'POST':
        sender_name = request.POST.get('sender_name')
        sender_email = request.POST.get('sender_email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        Message.objects.create(sender_email=sender_email,
                               sender_name=sender_name,
                               phone=phone,
                               message=message)

        return JsonResponse({'msg': 'success', 'status': 1})

    return JsonResponse({'msg': 'no message', 'status': 0 })














