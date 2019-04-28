from django.db import models
from DjangoUeditor.models import UEditorField
from DjangoUeditor.commands import *

class articles(models.Model):
    page = UEditorField('内容', height=300, width=1000, default=u'', blank=True, imagePath="upload/imgs/", toolbars='besttome', filePath='upload/files/')
    author = models.CharField(u'作者', max_length=30)
    def __str__(self):
        return self.author+'的文章'

# Create your models here.
class person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.name




class Blog(models.Model):
    Name = models.CharField(u'姓名', max_length=100, blank=True)
    Description = UEditorField(u'描述', blank=True, toolbars="full")
    ImagePath = models.CharField(u'图片目录', max_length=100, blank=True)
    Content = UEditorField(u'内容', height=200, width=500, default='test', imagePath="upload/imgs/",toolbars="mini",
                           filePath='bb/', blank=True, settings={"a": 2})
