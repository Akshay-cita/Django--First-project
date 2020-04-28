from django.urls import path,re_path
from accounts import views

urlpatterns=[
path('signup/',views.signup_view,name="signup"),
path('new/',views.user_account,name="new"),

]
