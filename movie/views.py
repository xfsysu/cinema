from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserLoginForm, UserRegisterForm

def index(request):
	return render(request, 'base.html')


def login_view(request):
	title = "Login"
	print (request.user.is_authenticated())
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get('username')
		password = form.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		login(request, user)
		if next:
			return redirect(next)
		return redirect("/")
	context = {
		'form': form,
		'title': title
	}
	return render(request, 'form.html', context)

def register_view(request):
	print (request.user.is_authenticated())
	next = request.GET.get('next')
	title = 'Register'
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		if next:
			return redirect(next)
		return redirect('/')

	context = {
		'form': form,
		'title': title
	}
	return render(request, 'form.html', context)

def logout_view(request):
	logout(request)
	return redirect("/")


