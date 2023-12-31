from django.urls import path
from ServiceApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # For Services
    path('', views.index),
    path('create_service/', views.ServiceCreateApi.as_view(), name='create_service'),
    path('service/<int:pk>/update', views.ServiceUpdateApi.as_view(), name='update_service'),
    path('service/<int:pk>/delete', views.ServiceDeleteApi.as_view(), name='delete_service'),

    # For Customers
    path('customer_orders/', views.customer_orders, name='orders'),
    path('create_order/', views.CustomerCreateApi.as_view(), name='create_order'),
    path('<int:pk>/update', views.CustomerUpdateApi.as_view(), name='update_order'),
    path('<int:pk>/delete', views.CustomerDeleteApi.as_view(), name='delete_order'),

    # For Postman
    # path('service/', views.TypeServiceApi),
    # path('service/<int:pk>', views.TypeServiceApi),
    # path('customer/', views.CustomerApi),
    # path('customer/<int:pk>', views.CustomerApi, name='delete'),
    # path('service/savefile/<int:pk>', views.SaveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
