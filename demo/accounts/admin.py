# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import BlogUser
from django.contrib import admin


class BlogUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nickname')
    list_display_links = ('id', 'nickname')


admin.site.register(BlogUser, BlogUserAdmin)