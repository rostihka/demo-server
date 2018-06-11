# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.six import python_2_unicode_compatible
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.timezone import now
from django.urls import reverse


@python_2_unicode_compatible
class BlogUser(AbstractBaseUser):
    nickname = models.CharField(max_length=100, blank=True)
    mugshot = models.ImageField(upload_to='upload/mugshots', blank=True)
    created = models.DateTimeField(default=now)
    last_mod_time = models.DateTimeField(default=now)

    def get_absolute_url(self):
        return reverse('blog:autor_detail', kwargs={'author_name': self.username})

    def __str__(self):
        return self.email