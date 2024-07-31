from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class TODO(models.Model):
    choicesStatus = [
        ("C","COMPLETED"),
        ("P","PENDING"),
    ]
    priority = [
        ("1","one"),
        ("2","two"),
        ("3","three"),
        ("4","four"),
        ("5","five"),
        ("6","six"),
        ("7","seven"),
        ("8","eight"),
        ("9","nine"),
        ("10","ten")
    ]
    title= models.CharField(max_length=60)
    status = models.CharField(max_length=2,choices=choicesStatus)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=2,choices=priority)

    def __str__(self):
        return self.title




