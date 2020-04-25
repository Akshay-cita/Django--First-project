from django.urls import path
from firstapp import views

urlpatterns=[
    path('firstapp',views.index,name='index'),

]
