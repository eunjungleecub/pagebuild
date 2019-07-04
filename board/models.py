from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200, null=False)
    author = models.CharField(max_length=20, null=True)
    date_published = models.DateTimeField(auto_now=False, auto_now_add=True)
    files = models.FileField(default=None, upload_to='files', blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gallery_detail', kwargs={'pk': self.pk})