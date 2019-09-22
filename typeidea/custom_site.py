#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jiang Feng"
# Date: 2019/4/22


from django.contrib.admin import AdminSite

class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea管理后台'
    index_title = '首页'

custom_site = CustomSite(name='cus_admin')