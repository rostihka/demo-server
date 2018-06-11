# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.six import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    created = models.TimeField()
    updated = models.TimeField()


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name[:20]


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return  self.name[:20]


@python_2_unicode_compatible
class Article(Base):
    class Meta:
        ordering = ['-created']
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to='img/blog')
    views = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title[:20]

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])



