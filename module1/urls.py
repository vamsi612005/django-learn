from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello/', hello, name='Hello'),
    path('',newhomepage,name='newhomepage'),
    path('travelpackage/',travelpackage,name='travelpackage'),
    path('print/',print_to_console,name="print_to_console"),
    path('p/',print1,name="print1"),
    path('randomcall/',randomcall,name="randomcall"),
    path('randomlogic/',randomlogic,name="randomlogic"),
    path('get_date/',get_date,name="get_date"),
    path('reglogin/',reglogin,name='reglogin'),
    path('regcall/',regcall,name='regcall'),
    path('pie_chart/',pie_chart,name='pie_chart'),
    path('front/',front,name='front'),
    path('weatherpagecall/',weatherpagecall,name='weatherpagecall'),
    path('weatherlogic/',weatherlogic,name='weatherlogic'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('login1', login1, name='login1'),
    path('signup1', signup1, name='signup1'),
    path('logout', logout, name='logout'),







]
