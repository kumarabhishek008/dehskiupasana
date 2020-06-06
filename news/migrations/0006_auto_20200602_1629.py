# Generated by Django 3.0.5 on 2020-06-02 10:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20200602_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='anonymous', max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='feeds',
            name='date_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 2, 16, 29, 35, 697935)),
        ),
    ]
