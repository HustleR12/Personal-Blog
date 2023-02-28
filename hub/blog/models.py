from django.db import models
import django.utils

class Post(models.Model):

    sno = models.AutoField(primary_key=True)  
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=25)
    slug = models.CharField(max_length=40)
    timeStamp = models.DateField( default=django.utils.timezone.now)

    def __str__(self):
        return self.title + " by " + self.author + " @ : " + str(self.timeStamp)
