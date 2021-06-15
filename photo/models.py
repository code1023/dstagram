from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Photo(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_photo')
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_date']

    def __str__(self):
        return f'{self.author.username} {self.created_date.strftime("%Y-%m-%d %H:%M:%S")}'

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])
