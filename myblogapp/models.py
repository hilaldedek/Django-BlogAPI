from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=32)
    def __str__(self):
        return self.name

class Post(models.Model):
    user=models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,default=1,on_delete=models.CASCADE)
    title=models.CharField(max_length=32)
    text=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title+' '+self.created_date
    
