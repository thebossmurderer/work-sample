# Generated by Django 4.2.3 on 2023-08-08 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='siteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteName', models.CharField(max_length=200, verbose_name='نام سایت')),
                ('siteUrl', models.CharField(max_length=200, verbose_name='دامنه سایت')),
                ('address', models.CharField(max_length=200, verbose_name='آدرس سایت')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='تلفن سایت')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='ایمیل سایت')),
                ('copyRight', models.TextField(verbose_name='متن کپی رایت سایت')),
                ('siteLogo', models.ImageField(upload_to='images/siteSetting/', verbose_name='لوگوی سایت')),
                ('aboutUsText', models.TextField(verbose_name='متن درباره ما سایت')),
                ('isMainSetting', models.BooleanField(verbose_name='تنظیمات اصلی')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'تنظیمات سایت',
            },
        ),
    ]