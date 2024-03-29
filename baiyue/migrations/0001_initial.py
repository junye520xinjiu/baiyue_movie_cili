# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-07-11 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Md_link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('magnetic_link', models.CharField(max_length=150, null=True, verbose_name='磁力下载连接')),
            ],
            options={
                'verbose_name_plural': '磁力下载链接表',
                'verbose_name': '磁力下载链接表',
                'db_table': 'Magnetic_link',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(db_index=True, max_length=100, null=True, verbose_name='电影名称')),
                ('release_time', models.CharField(db_index=True, max_length=100, null=True, verbose_name='上映时间')),
                ('file_size', models.CharField(db_index=True, max_length=100, null=True, verbose_name='文件大小')),
                ('act_role', models.CharField(db_index=True, max_length=400, null=True, verbose_name='主演')),
                ('md_link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baiyue.Md_link')),
            ],
            options={
                'verbose_name_plural': '电影信息',
                'verbose_name': '电影表',
                'db_table': 'Movie',
            },
        ),
    ]
