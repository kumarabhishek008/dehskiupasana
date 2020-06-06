from django.db import models
import datetime
# Create your models here.
class feeds(models.Model):
    news_choice =(('crime','crime'),
                  ('sports','sports'),
                  ('film','film'),
                  ('politics','politics'),
                  ('city','city'),
                  ('country','country'))
    category = models.CharField(max_length=100,choices=news_choice,default='choice')
    title = models.CharField(max_length=100,default='latest news')
    description = models.CharField(max_length=2000,default='my news')
    caption = models.CharField(max_length=50,default='news')
    file = models.FileField(upload_to='feeds',default='default.jpg')
    date_time = models.DateTimeField('pubdate',default=datetime.datetime.now())

class file(models.Model):
    daily_paper = models.FileField(upload_to='news_paper')

class contactus(models.Model):
    name = models.CharField(max_length=100,default='anonymous')
    email = models.EmailField()
    comment = models.TextField()
