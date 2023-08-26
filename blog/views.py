from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def index(request):
	posts = Post.objects.all() #getting all data from our data 
	context = {'posts':posts}
	return render(request,'index.html',context) #passing data to template

def detail_view(request,pk):
	post = Post.objects.get(id=pk)
	context={'post':post}
	return render(request,'postdetail.html',context)