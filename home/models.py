from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    status_choices=[('C','Completed'),('P','Pending')]
    title=models.CharField(max_length=50)
    status=models.CharField(max_length=2,choices=status_choices)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    