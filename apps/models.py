from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    time_now = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='images', blank=True, null=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    subject = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name