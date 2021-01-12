from django.db import models

# Create your models here.


# 用户表
class User(models.Model):
    username = models.CharField(blank=False, max_length=64, verbose_name="用户名", unique=True)
    password = models.CharField(blank=False, max_length=64, verbose_name="密码", unique=False)

    def __str__(self):
        return "{} => {}".format(self.username, self.password)
