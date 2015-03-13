# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='databaseImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('fileName', models.TextField(max_length=100)),
                ('mime_type', models.TextField(max_length=20)),
                ('filePath', models.TextField(max_length=50)),
                ('imgTitle', models.TextField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
