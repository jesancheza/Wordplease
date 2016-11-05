# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20161103_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(default='PUB', max_length=10, choices=[('PUB', 'Public'), ('PRIV', 'Private')]),
        ),
    ]
