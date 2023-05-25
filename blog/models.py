from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    #tag
    category=models.ManyToManyField(Category)
    author=models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image=models.ImageField(upload_to='blog/', default='blog/default.jpg')
    counted_views =models.IntegerField(default=0)
    status= models.BooleanField(default=False)
    published_date=models.DateTimeField(null=True)
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)

    class Meta:
        #ordering =['created_date']
        verbose_name ='post'
    def __str__(self):
        return self.title
    
    def snippets(self):
        return self.content[:100]+'...'




    # @property
    # def is_future(self):
    #     if self.publishing_date > timezone.now():
    #         return True
    #     return False