# Generated by Django 4.2.3 on 2023-08-10 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articleCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان دسته بندی')),
                ('urlTitle', models.CharField(max_length=200, unique=True, verbose_name='عنوان در url')),
                ('isActive', models.BooleanField(default=True, verbose_name='فعال / غیر فعال')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articleModule.articlecategories', verbose_name='دسته بندی والد')),
            ],
            options={
                'verbose_name': 'دسته بندی مقاله',
                'verbose_name_plural': 'دسته بندی های مقالات',
            },
        ),
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان مقاله')),
                ('slug', models.SlugField(allow_unicode=True, max_length=400, verbose_name='عنوان در url')),
                ('image', models.ImageField(upload_to='images/articles', verbose_name='تصویر مقاله')),
                ('shortDescription', models.TextField(verbose_name='توضیحات کوتاه')),
                ('text', models.TextField(verbose_name='متن مقاله')),
                ('isActive', models.BooleanField(default=True, verbose_name='فعال / غیر فعال')),
                ('selectedCategories', models.ManyToManyField(to='articleModule.articlecategories', verbose_name='دسته بندی ها')),
            ],
            options={
                'verbose_name': 'مقاله',
                'verbose_name_plural': 'مقالات',
            },
        ),
    ]
