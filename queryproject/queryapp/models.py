from django.db import models
from django.conf import settings
from django.utils.text import slugify 
from django.urls import reverse


# Create your models here.

class Şehirler(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    şehir = models.CharField(max_length=100000)
    
    def __str__(self):
        return self.şehir

class Devlet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    ülke = models.CharField(max_length=100)
    başkent = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.ülke)
        super(Devlet, self).save(*args, **kwargs)

    def __str__(self):
        return self.ülke
    
    def get_absolute_url(self):
        return reverse('queryapp:details', args=[self.slug])
    