from django.db import models

# Create your models here.


class UserModel(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=64)

    class Meta:
        db_table = 'user'   # 重定义表明
        db_table_comment = "用于存储用户信息的数据集表"  # 数据库表的注释
        ordering = ["-id"]  # 或许对象列表时的排序  负号 表示倒序

