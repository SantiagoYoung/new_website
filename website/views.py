from django.shortcuts import render
from .models import Service,Portfolio,Carousel_figure,Client_words
import json
from django.http import JsonResponse, HttpResponse


def all_service(request):

    services = Service.objects.all().order_by('is_featured')
    l = []
    for service in services:
        d = {}
        d['name'] = service.name
        d['description'] = service.description
        d['thumbnail'] = service.thumbnail

    data = json.dumps(l)

    return HttpResponse(data, content_type='application/json')


def feature_service(request):

    feature_services = Service.objects.filter(is_featured=True)

    l = []
    for service in feature_services:
        d = {}
        d['name'] = service.name
        d['description'] = service.description
        d['thumbnail'] = service.thubnail
        # d['is_featured'] = service.is_featured
        l.append(d)

    data = json.dumps(l)

    return HttpResponse(data,content_type='application/json')


def carousel_figure(request):

    carousels = Carousel_figure.objects.all().order_by('-create_time')[0:3]

    l =[]
    for carousel in carousels:
        d = {}
        d['title'] = carousel.title
        d['piture'] = carousel.piture
        d['description'] = carousel.description
        l.append(d)

    data = json.dumps(l)

    return HttpResponse(data,content_type='application/json')


def portfolio(request):

    portfolios = Portfolio.objects.filter(display=True).order_by('-create_time')[0:6]

    l = []
    for portfolio in portfolios:
        d = {}
        d['name'] = portfolio.name
        d['description'] = portfolio.description
        d['id'] = portfolio.id
        l.append(d)
    data = json.dumps(l)

    return HttpResponse(data,content_type='application/json')



def client_words(request):

    words = Client_words.objects.filter(display=True)[0:3]

    l = []
    for word in words:
        d = {}
        d['title'] = word.title
        d['client_name'] = word.client_name
        d['client_title'] = word.client_title
        d['client_company'] = word.client_company
        d['picture'] = word.picture
        l.append(d)

    data = json.dumps(l)

    return HttpResponse(data, content_type='application/json')















