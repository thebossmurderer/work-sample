# Generated by Django 4.2.3 on 2023-07-30 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0010_alter_productbrand_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/products', verbose_name='تصویر محصول'),
        ),
    ]