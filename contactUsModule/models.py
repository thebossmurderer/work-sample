from django.db import models


# Create your models here.


class contactUs(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    fullName = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    message = models.TextField(max_length=300, verbose_name='متن تماس با ما')
    createdDate = models.DateTimeField(verbose_name='تاریح ایجاد', auto_now_add=True)
    response = models.TextField(verbose_name='متن پاسخ تماس با ما',null=True,blank=True)
    isReadByAmin = models.BooleanField(verbose_name='خوانده شده توسط ادمین',default=False)

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'لیست تماس با ما'

    def __str__(self):
        return self.title
