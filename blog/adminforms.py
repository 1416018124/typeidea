#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Jiang Feng"
# Date: 2019/4/22

from django import forms

class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)