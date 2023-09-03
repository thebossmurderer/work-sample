from django.db import models


# Create your models here.


class siteSetting(models.Model):
    siteName = models.CharField(max_length=200, verbose_name='نام سایت')
    siteUrl = models.CharField(max_length=200, verbose_name='دامنه سایت')
    address = models.CharField(max_length=200, verbose_name='آدرس')
    phone = models.CharField(max_length=200, null=True, blank=True, verbose_name='تلفن')
    email = models.CharField(max_length=200, null=True, blank=True, verbose_name='ایمیل')
    copyRight = models.TextField(verbose_name='متن کپی رایت سایت')
    siteLogo = models.ImageField(upload_to='images/siteSetting/', verbose_name='لوگوی سایت')
    aboutUsText = models.TextField(verbose_name='متن درباره ما سایت')
    isMainSetting = models.BooleanField(verbose_name='تنظیمات اصلی')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات سایت'

    def __str__(self):
        return self.siteName


class footerLinksBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته بندی لینک در فوتر'
        verbose_name_plural = 'دسته بندی های لینک در فوتر'

    def __str__(self):
        return self.title


class footerLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    footerLinkBox = models.ForeignKey(to=footerLinksBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'لینک در فوتر'
        verbose_name_plural = 'لینک ها در فوتر'

    def __str__(self):
        return self.title


class slider(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=200, verbose_name='لینک')
    urlTitle = models.CharField(max_length=200, verbose_name='عنوان لینک')
    description = models.TextField(verbose_name='توضیحات اسلایدر')
    image = models.ImageField(upload_to='images/sliders', verbose_name='تصویر اسلایدر')
    isActive = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    class Meta:
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title


class siteBanner(models.Model):
    class siteBannerPositions(models.TextChoices):
        productList = 'productList', 'صفحه لیست محصولات',
        productDetial = 'productDetail', 'صفحه جزئیات محصولات',
        aboutUs = 'aboutUs', 'صفحه درباره ما',

    title = models.CharField(max_length=200, verbose_name='عنوان بنر')
    url = models.URLField(max_length=400, null=True, blank=True, verbose_name='آدرس بنر')
    image = models.ImageField(upload_to='images/banners', verbose_name='تصویر بنر')
    isActive = models.BooleanField(verbose_name='فعال / غیر فعال')
    position = models.CharField(max_length=200, choices=siteBannerPositions.choices, verbose_name='جایگاه نمایشی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'بنر تبلیغاتی'
        verbose_name_plural = 'بنرهای تبلیغاتی'
