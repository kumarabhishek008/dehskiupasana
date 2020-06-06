from django.shortcuts import render,redirect
from .models import *
from django.core.mail import send_mail


def index(request):
    crimefeed = feeds.objects.filter(category='crime').order_by('date_time').reverse()[:6]
    sportsfeed = feeds.objects.filter(category='sports').order_by('date_time').reverse()[:6]
    filmfeed = feeds.objects.filter(category='film').order_by('date_time').reverse()[:6]
    politicsfeed = feeds.objects.filter(category='politics').order_by('date_time').reverse()[:6]
    cityfeed = feeds.objects.filter(category='city').order_by('date_time').reverse()[:6]
    countryfeed = feeds.objects.filter(category='country').order_by('date_time').reverse()[:6]
    news_paper = file.objects.order_by('daily_paper').reverse()[:1]
    return render(request,'news/index.html',{'crimefeed':crimefeed,'sportsfeed':sportsfeed,'filmfeed':filmfeed,'politicsfeed':politicsfeed,'cityfeed':cityfeed,'countryfeed':countryfeed,'news_paper':news_paper})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comments']
        contact_us = contactus(name = name,email = email,comment=comment)
        contact_us.save()
        contact_us=contactus.objects.all()
        subject ='SUBSCRIBED'
        message= 'you have subscribed'
        from_email = '2012abhishekquicker@gmail.com'
        send_mail(subject,message,from_email,contact_us.email,fail_silently=False)
    return redirect('/')
def details(request,pk):
    detail = feeds.objects.filter(id=pk)
    return render(request,'news/detail.html',{'detail':detail})
def read_more(request,category):
    read = feeds.objects.filter(category=category).order_by('date_time').reverse()
    return render(request,'news/readmore.html',{'read':read})