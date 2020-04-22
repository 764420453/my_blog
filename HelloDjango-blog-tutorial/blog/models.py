from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# 分类
class Category(models.Model):
    """
    分类id     分类名
    """
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    """
    标签id     表桥名
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    """
    文章id    标题    正文    发表时间  分类    标签
    """
    title=models.CharField(max_length=70)
    body=models.TextField()

    create_time=models.DateField()    #创建时间
    modified_time=models.DateField()  #最后修改时间
    excerpt=models.CharField(max_length=200,blank=True)  #文章摘要

    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    tags=models.ManyToManyField(Tag,blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title