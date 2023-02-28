from django.db import models
import django.utils

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100, default='xyz@gmail.com')
    content = models.TextField()
    timeStamp = models.DateField( default=django.utils.timezone.now)

    def __str__(self):
        return "entry from " + self.name + " @ : " + str(self.timeStamp)
     