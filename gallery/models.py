from django.db import models

# Create your models here.


class Gallery(models.Model):  # 创建一个功能模块，即菜谱
    description = models.CharField(default='在这里写作品的简介',max_length=100)  #显示简单描述
    image = models.ImageField(default='default.png', upload_to='images/')  #upload_to上传到哪里
    title = models.CharField(default='作品标题',max_length=100)

    #可以修改名称
    def __str__(self):
        return self.title

    
