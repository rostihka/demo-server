# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.utils.six import python_2_unicode_compatible
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Base(models.Model):
    class Meta:
        abstract = True

    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()

        self.updated = timezone.now()
        return super(Base, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Category(Base):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('blog:category_detail', kwargs={'category_name': self.slug})

    def __str__(self):
        return self.name[:20]


@python_2_unicode_compatible
class Tag(Base):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name[:20]


@python_2_unicode_compatible
class Article(Base):
    class Meta:
        ordering = ['-created']

    STATUS_CHOICES = (
        ('d', 'part'),
        ('p', 'publised')
    )

    title = models.CharField(max_length=50, unique=True)
    body = models.TextField()
    image = models.ImageField(upload_to='img/blog', null=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    topped = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=False)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title[:20]

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])


@python_2_unicode_compatible
class Comment(Base):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()

    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]

