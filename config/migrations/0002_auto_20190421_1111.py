# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-04-21 03:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post',
            new_name='SideBar',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='owner',
        ),
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': '友链', 'verbose_name_plural': '友链'},
        ),
        migrations.RemoveField(
            model_name='link',
            name='is_nav',
        ),
        migrations.RemoveField(
            model_name='link',
            name='name',
        ),
        migrations.AddField(
            model_name='link',
            name='href',
            field=models.URLField(default='', verbose_name='链接'),
        ),
        migrations.AddField(
            model_name='link',
            name='title',
            field=models.CharField(default='', max_length=255, verbose_name='标题'),
        ),
        migrations.AddField(
            model_name='link',
            name='weight',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1, help_text='权重高展示顺序靠前', verbose_name='权重'),
        ),
        migrations.AlterField(
            model_name='link',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='config_Tag_owner', to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
