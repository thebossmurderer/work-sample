# Generated by Django 4.2.3 on 2023-08-17 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountModule', '0005_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='آدرس'),
        ),
    ]
