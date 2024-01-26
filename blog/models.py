from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify
from django.contrib.auth.models import User



# Create your models here.

class blogmodel(models.Model):
    title = models.CharField(max_length = 30)
    content = HTMLField()
    slug = models.SlugField(null = True,blank = True)
    image = models.ImageField(upload_to='blog/image')
    created_at = models.DateTimeField(auto_now_add = True)
    upload_to = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.title
    # for genrate slug automaticly
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(blogmodel,self).save(*args,**kwargs)