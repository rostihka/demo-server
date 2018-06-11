# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Article
from serializers import ArticleSerializer
from django.http import JsonResponse


def article_list(request):
    article = Article.objects.all()
    serializer = ArticleSerializer(article, many=True)
    return JsonResponse(serializer.data, safe=False)
