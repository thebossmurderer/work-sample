# Generated by Django 4.2.3 on 2023-08-13 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountModule', '0004_user_aboutuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile', verbose_name='تصویر اواتار'),
        ),
    ]