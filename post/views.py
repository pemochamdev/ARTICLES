from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q


from authy.models import Profile

from post.models import Category, Post, Tags
from post.forms import ContactForm

def index(request):

    posts = Post.objects.filter(status = 'published').order_by('publication_date')
    categories = Category.objects.all()


    #Search
    query = request.GET.get('q')
    if query:
        posts = posts.filter(Q(title__icontains = query) | Q(content__icontains = query)| Q(author__icontains = query)).distinct()

    
    
    #Pagination
    paginator  = Paginator(posts, 4)
    page_number = request.GET.get('page')
    posts_paginator = paginator.get_page(page_number)

  

    context = {
        'posts':posts_paginator,
        'categories':categories,
    }

    return render(request, 'index.html', context)


def category_views(request, category_slug):

    categories = Category.objects.all()
    posts = Post.objects.filter(status = 'published').order_by('publication_date')
    if category_slug:
        category  = get_object_or_404(Category, slug = category_slug)
        post = posts.filter(category = category)

    context = {
        'post':post,
        'categories':categories,
        'category':category,
    }

    return render(request, 'category.html', context)



def tag_views(request, tag_slug):

    posts = Post.objects.filter(status = 'published').order_by('publication_date') 
    tags = Tags.objects.all()
    if tag_slug:
        tag = get_object_or_404(Tags, slug = tag_slug)
        post = posts.filter(tags = tag)
    
    context = {
        'post':post,
        'tags':tags,
        'posts':posts,
    }

    return render(request, 'tags.html', context)



def post_detail_views(request, post_slug):
    user = request.user.id
    profile = Profile.objects.get(user__id=user)
    
    if post_slug:        
        post = get_object_or_404(Post, slug = post_slug)  

    # For the color of favorites button
    if profile.favorites.filter(slug = post_slug).exists():
        favorited = True
    else:
        favorited = False

    if request.method =='POST':
        if profile.favorites.filter(slug = post_slug).exists():
            profile.favorites.remove(post)
        else:
            profile.favorites.add(post)
    context = {
        'post':post,                
        'favorited':favorited,
    }

    return render(request, 'post_details.html', context)


def contact_form_views(request):

    if request.method == 'POST':
        form = ContactForm(request.POST or None)

        if form.is_valid():
            message = form.save(commit=False)
            message.message_date = timezone.now()
            form.save()
            return HttpResponseRedirect('contactsuccess')
        else:
            form = ContactForm()
            messages.error(request, 'Invalid form')
    else:
        form = ContactForm()
        messages.info(request, 'Please try again')

    context = {
        'form':form
    }
    return render(request, 'contact.html', context)


def contact_success(request):

    return render(request, 'contactsuccess.html')