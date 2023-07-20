from django.urls import path
from ServiceApp import views

urlpatterns = [
    path('service/', views.TypeServiceApi),
    path('service/<int:pk>', views.TypeServiceApi)
]
