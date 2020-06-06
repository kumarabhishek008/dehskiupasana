# Generated by Django 3.0.5 on 2020-06-02 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20200602_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeds',
            name='category',
            field=models.CharField(choices=[('crime', 'crime'), ('sports', 'sports'), ('film', 'film'), ('politics', 'politics'), ('city', 'city'), ('country', 'country')], default='choice', max_length=100),
        ),
        migrations.AlterField(
            model_name='feeds',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 2, 15, 39, 59, 370538)),
        ),
        migrations.AlterField(
            model_name='feeds',
            name='title',
            field=models.CharField(default='latest news', max_length=100),
        ),
    ]
