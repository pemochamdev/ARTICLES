from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe


from ckeditor_uploader.fields import RichTextUploadingField

STATUS_CHOICES = (
    ('draf', 'Draft'),
    ('published', 'Published'),
    ('rejeted', 'Rejeted')
)


def user_directory_path(instance, files):
    return 'user_{0}/{1}'.format(instance.user.id, files)


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    slug = models.SlugField(unique=True, max_length=200)

    class Meta:
      
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("category-post", kwargs={"slug": self.slug})
    
    



class Tags(models.Model):
    title = models.CharField(max_length=200, verbose_name='Tag')
    slug = models.SlugField(unique=True, max_length=200)

    class Meta:
        verbose_name = 'Tags'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("tag-post", args={self.slug})
    
    

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='Status')
    publication_date = models.DateTimeField(verbose_name='Published', auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='post_category', verbose_name='Category')
    picture = models.ImageField(upload_to=user_directory_path,blank=True, null=True, verbose_name='Picture', default= 'images/profile.png')
    content = RichTextUploadingField(verbose_name='Content')
    author = models.CharField(default='Anonymous', verbose_name='Create by', max_length=30)
    tags = models.ManyToManyField(Tags)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("detail-post", kwargs={"slug": self.slug})



    def post_image(self):
        return mark_safe('<img src="%s" with="50" height="50" />' % (self.picture.url))

    

    


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message_date = models.DateTimeField(auto_now_add=True)
    message = RichTextUploadingField(max_length=3000)


    class Meta:       
        verbose_name_plural = 'Contacts'


    def __str__(self):
        return (self.name + self.email)
    

    
