from . import views
from django.urls import path

from .views import *

urlpatterns = [
    path('', views.send_emails, name='send_emails'),
    path('contact123/', contact123, name='contact123'),
    path('contactmail/', contactmail, name='contactmail'),

]
