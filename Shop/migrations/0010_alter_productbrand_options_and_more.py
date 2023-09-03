# Generated by Django 4.2.1 on 2023-07-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0009_productbrand_product_brand'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productbrand',
            options={'verbose_name': 'سازنده', 'verbose_name_plural': 'سازندگان'},
        ),
        migrations.AlterField(
            model_name='productbrand',
            name='brandName',
            field=models.CharField(max_length=300, verbose_name='نام سازنده'),
        ),
    ]
