from django.urls import path
from ServiceApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('service/', views.TypeServiceApi),
    path('service/<int:pk>', views.TypeServiceApi),
    path('customer/', views.CustomerApi),
    path('customer/<int:pk>', views.CustomerApi),
    path('service/savefile/<int:pk>', views.SaveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
