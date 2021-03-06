# instablog/urls.py
from django.conf.urls import url
from django.contrib import admin

from blog import views as blog_views


urlpatterns = [
    url(r'^posts/create/$', blog_views.create_post, name='create_post'),
    url(r'^$', blog_views.list_posts),
    url(
        r'^posts/(?P<pk>[0-9]+)/$', blog_views.view_post, name='view_post'
    ),
    url(r'^hello/$', blog_views.hello_with_template),
    url(r'^admin/', admin.site.urls),
]
