
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index),
    path('contact',views.contact),
    path('detail/<int:pk>',views.details),
    path('readmore/<slug:category>',views.read_more),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)