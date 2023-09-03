from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='images/profile', verbose_name='تصویر اواتار', null=True, blank=True)
    emailActiveCode = models.CharField(max_length=100, verbose_name='کد فعال سازی ایمیل')
    aboutUser = models.TextField(null=True, blank=True, verbose_name='درباره شخص')
    address = models.TextField(null=True,blank=True,verbose_name='آدرس')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.email
