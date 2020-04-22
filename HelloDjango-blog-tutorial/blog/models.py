from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# 分类
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    """
    分类id     分类名
    """
    name=models.CharField(max_length=100,verbose_name='分类名称')
    class Meta:
        verbose_name='分类'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    标签id     表桥名
    """
    name = models.CharField(max_length=100,verbose_name='标签名称')
    class Meta:
        verbose_name='标签'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

class Post(models.Model):
    """
    文章id    标题    正文    发表时间  分类    标签
    """
    title=models.CharField(max_length=70,verbose_name='文章标题')
    body=models.TextField(verbose_name='正文')

    create_time=models.DateField(default=timezone.now,verbose_name='创建时间')    #创建时间
    modified_time=models.DateField(verbose_name='修改时间')  #最后修改时间
    excerpt=models.CharField(max_length=200,blank=True,verbose_name='摘要')  #文章摘要

    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='分类')
    tags=models.ManyToManyField(Tag,blank=True,verbose_name='标签')
    author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')
    class Meta:
        verbose_name='文章'
        verbose_name_plural=verbose_name

    def save(self, *args,**kwargs):
        self.modified_time=timezone.now()
        super().save(*args,**kwargs)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail',kwargs={'pk':self.pk})