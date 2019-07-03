from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 100)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add = True)
