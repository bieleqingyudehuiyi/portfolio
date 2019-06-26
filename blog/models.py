from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(default='文章标题', max_length=50) # mc，blog标题
    date = models.DateField() #md，文章上传时间
    image = models.ImageField(default='default.png',upload_to='images/')  # 图片,mi但是打不出来
    text = models.TextField(default='正文')  # 正文，mt但是打不出来

    def __str__(self):  # 实现标题
        return self.title

    def short_text(self):  
        return self.text[:60] + '...'