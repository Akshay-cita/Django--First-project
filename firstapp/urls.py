from django.urls import path,re_path
from firstapp import views

urlpatterns=[
    path('firstapp',views.index,name='index'),
    re_path(r'^(?P<slug>[\w-]+)/$',views.blog_detail,name='detail'),

]
