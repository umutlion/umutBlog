# Generated by Django 3.0.7 on 2020-08-01 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200801_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subcontent',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]