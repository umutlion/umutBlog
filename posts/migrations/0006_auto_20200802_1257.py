# Generated by Django 3.0.7 on 2020-08-02 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200802_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
