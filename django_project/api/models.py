from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User',
                              related_name='posts',
                              on_delete=models.CASCADE)
    poster100x100 = models.CharField(max_length=200, default='', blank=True)
    poster100x125 = models.CharField(max_length=200, default='', blank=True)
    poster200x250 = models.CharField(max_length=200, default='', blank=True)
    poster300x100 = models.CharField(max_length=200, default='', blank=True)
    poster300x200 = models.CharField(max_length=200, default='', blank=True)
    poster400x200 = models.CharField(max_length=200, default='', blank=True)
    poster400x400 = models.CharField(max_length=200, default='', blank=True)
    poster600x300 = models.CharField(max_length=200, default='', blank=True)
    poster1200x400 = models.CharField(max_length=200, default='', blank=True)
    poster1920x500 = models.CharField(max_length=200, default='', blank=True)
    poster1920x900 = models.CharField(max_length=200, default='', blank=True)
    poster = models.CharField(max_length=200, default='', blank=True)

    class Meta:
        ordering = ['created']

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User',
                              related_name='comments',
                              on_delete=models.CASCADE)
    post = models.ForeignKey('Post',
                             related_name='comments',
                             on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User',
                              related_name='categories',
                              on_delete=models.CASCADE)
    posts = models.ManyToManyField('Post',
                                   related_name='categories',
                                   blank=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
