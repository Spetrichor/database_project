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
    path('patient/',views.patient,name='patient'),
    path('patient_query/', views.patient_query, name='patient_query'),
    path('patient/patient_information/',views.patient_information,name='patient_information')
    path('nurses/',views.nurses,name='nurses')
    path('information/',views.information,name='information')
    path('information/modify/',views.modify_information,name='modify_information')
    path('information/modify_confirm/',views.modify_information_confirm,name='modify_information_confirm')



    path('patient/', views.worker, name='worker'),
    path('patient_add/', views.worker_add, name='worker_add'),
    path('patient_add_confirm/', views.worker_add_confirm, name='worker_add_confirm'),
    url(r'worker_modify/(\d+)', views.worker_modify, name='worker_modify'),
    url(r'worker_delete/(\d+)', views.worker_delete, name='worker_delete'),
    path('department/', views.department, name='department'),
    path('training/', views.training, name='training'),
    path('recruitment/', views.recruitment, name='recruitment'),
    path('salary/', views.salary, name='salary'),
    path('reward/', views.reward, name='reward'),
    path('account/', views.account, name='account'),
]
