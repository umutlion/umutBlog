

from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return self.title

    def postCount(self):
        return self.posts.all().count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='uploads/', blank=True)
    quote = models.TextField()
    subtitle = models.CharField(max_length=150)
    subImage = models.ImageField(upload_to='uploads/', blank=True)
    adviceImage = models.ImageField(upload_to='uploads/', blank=True)
    subcontent = models.TextField()
    content = models.TextField()
    slug = models.SlugField(unique=True, editable=False)
    created = models.DateField('date publisehed')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title + " =>" + str(self.created)

    def commentCount(self):
        return self.comments.all().count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.post.title

class Comment(models.Model):
   post = models.ForeignKey(Post,on_delete=models.CASCADE,default=1,related_name="comments")
   user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default=1)

   content = models.TextField()

   created = models.DateField(auto_now_add=True)

   def __str__(self):
       return self.user.username + " => " + self.post.title

