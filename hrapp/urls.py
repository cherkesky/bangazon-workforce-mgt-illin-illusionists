from django.urls import path
from django.conf.urls import include
from hrapp import views
from .views import *

app_name = 'hrapp'
urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('employees/', employee_list, name='employee_list'),
    path('departments/', department_list, name='departments'), # TODO: update the context param and name value
    path('trainingprograms/', employee_list, name='employee_list'),
    path('computers/', employee_list, name='employee_list'),

]
