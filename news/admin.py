from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import feeds,file,contactus
AdminSite.site_title = 'Desh ki Upasana'
AdminSite.site_header= 'Desh ki Upasana'

admin.site.register(feeds)
admin.site.register(file)
admin.site.register(contactus)
# Register your models here.
