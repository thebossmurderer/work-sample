# Generated by Django 4.2.3 on 2023-09-02 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0015_productvisit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_categories', to='Shop.productcategory', verbose_name='نام دسته بندی'),
        ),
    ]
