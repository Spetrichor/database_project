from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('register_confirm/', views.register_confirm, name='register_confirm'),
    path('patient/', views.patient, name='patient'),
    path('patient_query/', views.patient_query, name='patient_query'),
    path('patient/add/', views.patient_add, name='patient/add'),
    path('patient/add/confirm', views.patient_add_confirm, name='patient/add/confirm'),
    path('patient/patient_information/<str:name>', views.patient_information, name='patient/patient_information'),
    path('nurses/', views.nurses, name='nurses'),
    path('information/', views.information, name='information'),
    path('information/modify/', views.modify_information, name='information/modify'),
    path('information/modify_confirm/', views.modify_information_confirm, name='information/modify_confirm'),
    path('report/', views.report, name='report'),
    path('report/confirm', views.report_confirm, name='report/confirm'),
]
