from django.db import models

# Create your models here.


class Gallery(models.Model):  # 创建一个功能模块，即菜谱
    description = models.CharField(max_length=100)  #显示简单描述
