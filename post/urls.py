from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('post/category/<category_slug>', views.category_views, name='category-post'),
    path('post/detail/<post_slug>', views.post_detail_views, name='detail-post'),
    path('tag/<tag_slug>', views.tag_views, name='tag-post'),

    # Contact
    path('contact/', views.contact_form_views, name='contact-post'),    
    path('contact/contactsuccess/', views.contact_success, name='contactsuccess'),
]