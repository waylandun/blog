from django.db import models


# Create your models here.
class Department(models.Model):
    title = models.CharField(verbose_name='部门标题', max_length=32)
    dh = models.CharField(verbose_name='部门代号', max_length=32, default=None)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)

    def __str__(self):
        return self.title



class UserInfo(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=16)
    password = models.CharField(verbose_name='密码', max_length=64)
    age = models.IntegerField(verbose_name='年龄')
    # max_digits 数字位数（整数+小数）,decimal_places小数位数
    # max_digits=10 decimal_places=2 ->整数部分最多有 8 位数字，小数部分最多有 2 位数字
    account = models.DecimalField(verbose_name='账户余额', default=0, max_digits=10, decimal_places=2)
    create_time = models.DateTimeField(verbose_name='入职时间')
    gender_choices = ((1, '男'), (2, '女'),)
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)

    # TODO 相应部门被删除时  on_delete
    # 级联删除
    # depart = models.ForeignKey(to="Department",to_field="id",on_delete=models.CASCADE)
    # 字段置空
    depart = models.ForeignKey(Department, to_field="id", on_delete=models.SET_NULL, null=True, blank=True)
