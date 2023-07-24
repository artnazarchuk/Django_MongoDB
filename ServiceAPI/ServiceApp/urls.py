from django.urls import path
from ServiceApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index),
    path('customer_orders/', views.customer_orders, name='orders'),
    # path('create_order/', views.create_order, name='create_order'),
    path('create_order/', views.CustomerCreateApi.as_view(), name='create_order'),
    path('<int:pk>/update', views.CustomerUpdateApi.as_view(), name='update_order'),
    path('<int:pk>/delete', views.CustomerDeleteApi.as_view(), name='delete_order'),
    path('service/', views.TypeServiceApi),
    path('service/<int:pk>', views.TypeServiceApi),
    path('customer/', views.CustomerApi),
    path('customer/<int:pk>', views.CustomerApi, name='delete'),
    path('service/savefile/<int:pk>', views.SaveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
