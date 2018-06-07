from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()

    def quickSummary(self):
        return self.summary[:100]

    def __str__(self):
        return self.title
