# Generated by Django 3.0.7 on 2020-08-01 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200801_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='quote',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
