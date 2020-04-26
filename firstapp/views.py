from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from firstapp.models import Post

def index(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    my_dict={'posts':posts}
    return render(request,'index.html',context=my_dict)

def blog_detail(request,slug):
    # return HttpResponse(slug)
    blog=Post.objects.get(slug=slug)
    return render(request,'article_detail.html',{'blogs':blog})



# Create your views here.
