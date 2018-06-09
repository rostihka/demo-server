# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Base(models.Model):
    created = models.TimeField()
    updated = models.TimeField()


class Article(Base):
    title = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return self.title[:20]


