# Generated by Django 4.2.3 on 2023-08-01 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountModule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirmPass',
            field=models.CharField(max_length=30, null=True, verbose_name='تایید رمز'),
        ),
    ]
