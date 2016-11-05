from django.shortcuts import render
from .models import News, Category, Tags
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from datetime import datetime

def _news(request, news):



    paginator = Paginator(news, 5)
    total_page = paginator.num_pages
    page = request.GET.get('page')
    try:
        news = paginator.page(page)
    except (PageNotAnInteger, InvalidPage):
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    l = []
    l.append(total_page)
    for new in news:
        d = {}
        d['id'] = new.id
        d['title'] = new.title
        d['content'] = new.content
        d['author'] = new.author
        d['click_num'] = new.click_num
        d['create_time'] = new.clean_create_time
        l.append(d)


    return JsonResponse(l)


def news(request):

    news = News.objects.filter(is_display=True).order_by('-create_time')

    return _news(request, news)


def archive(request):

    # news = News.objects.datetimes('create_time', 'month', order='DESC')

    archive = News.objects.archive()

    return JsonResponse(archive)


def archive_news(request):

    if request.method == 'POST':

        date = request.POST.get('date')

        news = News.objects.filter(create_time__icontains=date)

        return _news(request, news)

    return JsonResponse({'status': 0})


def tags(request):

    tags = Tags.objects.all()



































































