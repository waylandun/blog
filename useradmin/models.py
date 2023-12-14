from django.db import models

# Create your models here.


class UserModel(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=64)

    class Meta:
        db_table = 'user'
