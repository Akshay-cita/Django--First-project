from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from firstapp.models import Post,User
from firstapp.forms import NewUserform,form_view

def index(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    my_dict={'posts':posts}
    return render(request,'firstapp/index.html',context= my_dict)

def blog_detail(request,slug):
    # return HttpResponse(slug)
    blog=Post.objects.get(slug=slug)
    return render(request,'article_detail.html',{'blogs':blog})

def signup_view(request):
    form=form_view()
    if request.method =='POST':
        form=form_view(request.POST)
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
            return index(request)
        else:
            print("error/....")
    return render(request,'user.html',{'form':form})


# Create your views here.
