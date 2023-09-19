from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def userLogin(request):
	if request.user.is_authenticated:
		return redirect('home')
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username,password=password)

			if user is not None:
				login(request,user)
				messages.info(request,f"You are logged in as {username}")
				return redirect('home')
			else:
				messages.error(request,"Invalid username or password")

	return render(request,'accounts/login.html')


def userRegistration(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request,user)
			messages.success(request,'Registration Successful')
			return redirect('home')

		messages.error(request,"Unsuccessful Registration, Invalid information")

	form = NewUserForm(request.POST)
	context ={'form':form}
	return render(request,'accounts/register.html',context)


def userLogout(request):
	logout(request)
	return redirect('login')