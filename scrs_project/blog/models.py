from django.db import models

# Create your models here.
class Blog(models.Model):
    pub_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
