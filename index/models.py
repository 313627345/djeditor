from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from DjangoUeditor.forms import UEditorField
from wangeditor.fields import WangRichTextField

# Create your models here.


class Index(models.Model):
    name = models.CharField(max_length=100, verbose_name='名称')
    about = UEditorField(label='简洁')
    content = WangRichTextField()
    des = RichTextUploadingField(default='',verbose_name='')

    """记录时间"""
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        verbose_name = '信息管理'
        verbose_name_plural = verbose_name

    # 用于模型查询返回
    def __str__(self):
        return self.name