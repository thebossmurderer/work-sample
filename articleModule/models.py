from django.db import models
from accountModule.models import User
from jalali_date import date2jalali , datetime2jalali

# Create your models here.


class articleCategories(models.Model):
    parent = models.ForeignKey('articleCategories', null=True, blank=True, on_delete=models.CASCADE,
                               verbose_name='دسته بندی والد')
    title = models.CharField(max_length=200, verbose_name='عنوان دسته بندی')
    urlTitle = models.CharField(max_length=200, unique=True, verbose_name='عنوان در url')
    isActive = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی مقاله'
        verbose_name_plural = 'دسته بندی های مقالات'


class article(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان مقاله')
    slug = models.SlugField(max_length=400, db_index=True, allow_unicode=True, verbose_name='عنوان در url')
    image = models.ImageField(upload_to='images/articles', verbose_name='تصویر مقاله')
    shortDescription = models.TextField(verbose_name='توضیحات کوتاه')
    text = models.TextField(verbose_name='متن مقاله')
    isActive = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')
    selectedCategories = models.ManyToManyField(articleCategories,verbose_name='دسته بندی ها')
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='نویسنده',null=True,editable=False)
    createDateTime = models.DateTimeField(auto_now_add=True,editable=False,verbose_name='تاریخ ثبت')

    def __str__(self):
        return self.title


    def getJalaliCreateDate(self):
        return date2jalali(self.createDateTime)

    def getJalaliCtreateDateTime(self):
        return self.createDateTime.strftime('%H:%M')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


class articleComment(models.Model):
    article = models.ForeignKey(article,on_delete=models.CASCADE,verbose_name='مقاله')
    parent = models.ForeignKey('articleComment',null=True,blank=True,on_delete=models.CASCADE,verbose_name='والد')
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    createDate = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ثبت')
    text = models.TextField(verbose_name='متن نظر')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'نظر مقاله'
        verbose_name_plural = 'نظرات مقاله'



