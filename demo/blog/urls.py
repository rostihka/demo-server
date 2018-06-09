from django.conf.urls import url
from views import article_list

urlpatterns = [
    url(r'^blog/$', article_list),
]