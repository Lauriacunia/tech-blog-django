from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=10000)
    date_posted = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title + ' | ' + str(self.author) + ' | ' + str(self.date_posted) + ' | ' + self.content + ' | ' + str(self.id) + ' | ' 
