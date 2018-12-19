from django.db import models
from myaccount.models import Myuser as User

# Create your models here.

class log_users(models.Model):
    points=models.IntegerField()
    image=models.ImageField("upload image here",upload_to="users/")
    user=models.ForeignKey(User)

    def __str__(self):
        return self.points
