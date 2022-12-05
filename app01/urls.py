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
    path('patient/add/', views.patient_add, name='patient_add'),
    path('patient/add/confirm', views.patient_add_confirm, name='patient_add_confirm'),
    path('patient/patient_information/', views.patient_information, name='patient_information'),
    path('nurses/', views.nurses, name='nurses'),
    path('information/', views.information, name='information'),
    path('information/modify/', views.modify_information, name='modify_information'),
    path('information/modify_confirm/', views.modify_information_confirm, name='modify_information_confirm'),
    path('report/', views.report, name='report'),
    path('report/confirm', views.report_confirm, name='report_confirm'),
]
