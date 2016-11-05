# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Service,Portfolio,Carousel_figure,Client_words,Structure
import json
from django.http import JsonResponse, HttpResponse
from django.http import HttpResponse
import xlwt
import StringIO



def portfolio_page(request):

    return render(request, 'portfolio.html')

def service_page(request):

    return render(request, 'services.html')

def home_page(request):

    return render(request,'index.html')



def all_service(request):

    services = Service.objects.all().order_by('is_featured')

    # date = '2016'
    # services = Service.objects.filter(create_time__icontains=date)
    # print services, '>>>>>>>>'

    l = []
    for service in services:
        d = {}
        d['name'] = service.name
        d['description'] = service.description
        d['thumbnail'] = service.thumbnail.url
        l.append(d)
    data = json.dumps(l)

    return HttpResponse(data, content_type='application/json')
    # return JsonResponse({'data':l})


def feature_service(request):

    feature_services = Service.objects.filter(is_featured=True)[0:3]

    l = []
    for service in feature_services:
        d = {}
        d['name'] = service.name
        d['description'] = service.description
        d['thumbnail'] = service.thumbnail.url
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
        d['piture'] = carousel.piture.url
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
    # eva = Client_words.objects.datetimes('create_time', 'month', order='DESC')
    #
    # print eva,'>>>>>>>>>>>>>>>>>>>'

    l = []
    for word in words:
        d = {}
        d['title'] = word.title
        d['client_name'] = word.client_name
        d['client_title'] = word.client_title
        d['client_company'] = word.client_company
        d['picture'] = word.picture.url
        l.append(d)

    data = json.dumps(l)

    return HttpResponse(data, content_type='application/json')

def section(request):

    sections = Structure.objects.all()

    l = []
    for section in sections:
        d ={}
        d['section'] = section.section
        d['description'] = section.description
        l.append(d)
    data = json.dumps(l)

    return HttpResponse(data, content_type='application/json')





def excel_export(request):

    file_name = 'test.xls'
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=%s' % file_name

    ws = xlwt.Workbook(encoding='utf-8')
    sheet_w = ws.add_sheet(u'数据第一页')

    sheet_w.write(0, 0, 'id')
    sheet_w.write(0, 1, 'name')
    sheet_w.write(0, 2, 'descrip')
    sheet_w.write(0, 3, 'create_time')
    sheet_w.write(0, 4, 'edit_time')

    excel_row = 1

    services = Service.objects.all()

    for service in services:
        service_id = service.id
        service_name = service.name
        service_des = service.description
        service_create = service.create_time.strftime('%Y-%m')
        service_edit = service.edit_time.strftime('%Y-%m')

        sheet_w.write(excel_row, 0, service_id)
        sheet_w.write(excel_row, 1, service_name)
        sheet_w.write(excel_row, 2, service_des)
        sheet_w.write(excel_row, 3, service_create)
        sheet_w.write(excel_row, 4, service_edit)
        excel_row += 1


    output = StringIO.StringIO()
    ws.save(output)
    output.seek(0)
    response.write(output.getvalue())
    return response








