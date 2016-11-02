# -*- coding: utf-8 -*-s
from django.shortcuts import render
from .models import Facts, History, About_us, QnA
from django.http import HttpResponse
import json



def about_page(request):

    return render(request, 'about.html')




def about_us(request):

    about = About_us.objects.filter(display=True).order_by('?')[0]

    l = []
    # for about in abouts:
    d = {}
    d['title'] = about.title
    d['description'] = about.description
    d['picture'] = about.picture.url
    l.append(d)

    data = json.dumps(l)

    return HttpResponse(data, content_type='application/json')



def history(request):

    history = History.objects.all().order_by('year')

    l = []
    for history in history:
        d = {}
        d['year'] = history.year
        d['description'] = history.description
        l.append(d)
    data = json.dumps(l)

    return HttpResponse(data, content_type='application/json')


def facts(request):
    facts = Facts.objects.filter(display=True).order_by('-edit_time')[0:3]

    l = []
    for fact in facts:
        d = {}
        d['title'] = fact.title
        d['picture'] = fact.picture.url
        d['description'] = fact.description
        l.append(d)

    data = json.dumps(l)

    return HttpResponse(data, content_type='application/json')


def QandA(request):
    qnas = QnA.objects.filter(display=True).order_by('-create_time')[0:5]

    l = []
    for qna in qnas:
        d = {}
        d['question'] = qna.question
        d['answer'] = qna.answer
        l.append(d)
    data = json.dumps(l)

    return HttpResponse(data, content_type='application/json')







































