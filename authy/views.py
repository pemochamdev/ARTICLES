from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


from authy.models import Profile
from authy.forms import  SignupForm, ChangePasswordForm
from post.models import Post

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    posts = profile.favorites.all()
    
    
    #Pagination
    paginator  = Paginator(posts, 2)
    page_number = request.GET.get('page')
    posts_paginator = paginator.get_page(page_number)

    

    context = {
        'profile':profile,
        'posts':posts_paginator,

    }
    return render(request, 'authy/profile.html', context)


def sign_up(request):
    if request.method =='POST':
        form = SignupForm(request.POST or None)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')            
            User.objects.create_user(username=username, email=email, password=password)
            
            return redirect('login')
    #     else:
    #         form = SignupForm()
    #         messages.info(request, 'INVALID FORM')
    else:
        form = SignupForm()

    
    context = {
        'form':form,
    }
    return render(request, 'registration/sign_up.html', context)



@login_required
def PasswordChange(request):
	user = request.user
	if request.method == 'POST':
		form = ChangePasswordForm(request.POST)
		if form.is_valid():
			new_password = form.cleaned_data.get('new_password')
			user.set_password(new_password)
			user.save()
			update_session_auth_hash(request, user)
			return redirect('password_change_done')
	else:
		form = ChangePasswordForm(instance=user)

	context = {
		'form':form,
	}

	return render(request, 'registration/change_password.html', context)

def PasswordChangeDone(request):
	return render(request, 'registration/change_password_done.html')
