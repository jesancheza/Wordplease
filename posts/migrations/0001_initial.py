# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20150830_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=150)),
                ('summary', models.TextField(max_length=400)),
                ('body', models.TextField(default=b'')),
                ('image_url', models.URLField(default=b'', null=True, blank=True)),
                ('date_published', models.DateTimeField(default=b'')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('blog', models.ForeignKey(to='blogs.Blog')),
            ],
        ),
    ]
