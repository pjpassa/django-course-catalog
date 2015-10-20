# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('instructor', models.CharField(max_length=100)),
                ('duration', models.IntegerField(choices=[(2, '2 Weeks'), (8, '8 Weeks')])),
                ('courseArt', models.ImageField(upload_to='course_art')),
            ],
        ),
    ]
