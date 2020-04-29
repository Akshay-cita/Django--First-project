from django.urls import path,re_path
from firstapp import views


app_name='firstapp'

urlpatterns=[
    path('firstapp',views.index,name='index'),
    re_path(r'^(?P<slug>[\w-]+)/$',views.blog_detail,name=' blog_detail'),
    path('signup/',views.signup_view,name="signup"),
    path('new/',views.user_account,name="new"),

]
