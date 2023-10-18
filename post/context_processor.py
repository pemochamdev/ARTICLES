################ Author: https://github.com/pemochamdev #####################

from django.shortcuts import render

from .models import Category
from authy.models import Profile


def default(request):
    categories = Category.objects.all()
    profile = Profile.objects.all()

    context = {
        'categories': categories,
        'profile':profile,
    }
    return context