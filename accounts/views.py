from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from accounts.forms import NewUserform
# Create your views here.
def detailed(request):
    return render(request,'article_detail.html')

def signup_view(request):
    form=forms.form_view()
    if request.method =='POST':
        form=forms.form_view(request.POST)
        if form.is_valid():
            #do something here
            print("validation success")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])
    return render(request,"signup.html",{'form':form})

def user_account(request):
    form=NewUserform()
    if request.method =='POST':
        form=NewUserform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return detailed(request)
        else:
            print("error/....")
    return render(request,'user.html',{'form':form})
