from django.contrib import admin


from .models import Tags, Category, Post, Contact

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'author']
    ordering = ['-publication_date']
    list_display = ['title', 'category','author','status', 'post_image' ,'publication_date']



@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    ordering = ['-message_date']
    list_display = ['name', 'email', 'message_date', 'message']