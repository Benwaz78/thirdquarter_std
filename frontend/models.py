from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=100, verbose_name='Category Name')
    cat_desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.cat_name

    class Meta():
        verbose_name_plural='Category'

class Post(models.Model):
    pst_title = models.CharField(max_length=150)
    pst_image = models.ImageField(blank=True, null=True, upload_to='uploads/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pst_title

    @property
    def img_url(self):
        if self.pst_image:
            return self.pst_image.url
        



class Biography(models.Model):
    bio_img = models.ImageField(blank=True, verbose_name='Profile Image', null=True, upload_to='uploads/')
    bio_title = models.CharField(max_length=100, verbose_name='Profile Title')
    bio_description = models.TextField(verbose_name='Description')

    class Meta():
        verbose_name_plural = 'Biography'

    def __str__(self):
        return self.bio_title
=======

# Create your models here.
>>>>>>> fc2b3107a1a59876ede3fd3535367180c289c8e5
