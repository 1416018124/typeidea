"""typeidea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog.views import post_list, post_detail
from config.views import links
from typeidea.custom_site import custom_site

urlpatterns = [
    url(r'^super_admin/', custom_site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^$', post_list, name='post-list'),                                      #博客首页
    url(r'^category/(?P<category_id>\d+)/$', post_list, name='category-list'),        #分类列表页
    url(r'^tag/(?P<tag_id>\d+)/$', post_list, name='tag-list'),                  #标签列表页
    url(r'^post/(?P<post_id>\d+).html$', post_detail, name='post-detail'),           #博文详情页
    url(r'^links$', links, name='links'),                                      #友链展示页
]
