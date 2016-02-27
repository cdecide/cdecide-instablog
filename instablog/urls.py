from django.conf.urls import url
from django.contrib import admin

from blog import views as blog_views

urlpatterns = [
    url(r'^$', blog_views.list_posts),
    url(r'^hello/$', blog_views.hello_with_template),
    url(r'^admin/', admin.site.urls),
]