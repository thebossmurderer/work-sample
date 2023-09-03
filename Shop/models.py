# --------------------------------------------------- Library ----------------------------------------------------------
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
from accountModule.models import User

# ------------------------------------------------ Models Code ---------------------------------------------------------
################################################# Product Tags #########################################################
class productTags(models.Model):
    tag = models.CharField(max_length=30, verbose_name='تگ ها')

    def __str__(self):
        return f'{self.tag}'

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'


############################################### Product Categoty #######################################################
class productCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    urlTitle = models.CharField(max_length=300,db_index=True,null=True,verbose_name='عنوان در url')
    isDelete = models.BooleanField(default=False,verbose_name='حذف شده / نشده')
    isActive = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


############################################### Product Information ####################################################
class productInformation(models.Model):
    size = models.CharField(max_length=10, verbose_name='حجم')

    def __str__(self):
        return f'{self.size}'

    class Meta:
        verbose_name = 'اطلاعات تکمیلی'
        verbose_name_plural = 'اطلاعات تکمیلی'
############################################### Product Brand ##########################################################
class productBrand(models.Model):
    brandName = models.CharField(max_length=300,verbose_name='نام سازنده')
    urlTitle = models.CharField(max_length=300 , verbose_name='نام در url',db_index=True)
    isActive = models.BooleanField(default=False,verbose_name='فعال / غیر فعال')


    class Meta:
        verbose_name = 'سازنده'
        verbose_name_plural = 'سازندگان'

    def __str__(self):
        return self.brandName
################################################### Product ############################################################

class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام بازی')
    tags = models.ManyToManyField(productTags,verbose_name='تگ ها')
    category = models.ForeignKey(productCategory, on_delete=models.CASCADE, null=True, related_name='product_categories',
                                 verbose_name='نام دسته بندی')
    information = models.OneToOneField(productInformation, on_delete=models.CASCADE, null=True, blank=True,
                                       verbose_name='اطلاعات تکمیلی')
    image = models.ImageField(upload_to='images/products',null=True,blank=True,verbose_name='تصویر محصول')
    brand = models.ForeignKey(productBrand,on_delete=models.CASCADE,null=True,blank=True)
    price = models.FloatField(verbose_name='$ قیمت')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)], default=0,
                                 verbose_name='امتیاز')
    isActive = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')
    shortDescription = models.CharField(max_length=300, null=True,db_index=True, verbose_name='توضیحات کوتاه')
    description = models.TextField(verbose_name='توضیحات اصلی',null=True)
    slug = models.SlugField(default="", null=False, db_index=True , max_length=200,unique=True)
    isDelete = models.BooleanField(default=False,verbose_name='حذف شده / نشده')


    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def getAbsoluteUrls(self):
        return reverse('detailsPage', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}  ({self.price})"


class productVisit(models.Model):
    product = models.ForeignKey('Product',on_delete=models.CASCADE,verbose_name='محصول')
    ip = models.CharField(max_length=30,verbose_name='آیپی کاربر')
    user = models.ForeignKey(User,null=True,blank=True,verbose_name='کاربر',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product.title} / {self.ip}'

    class Meta:
        verbose_name = 'بازدید محصول'
        verbose_name_plural = 'بازدید های محصول'


class productGallery(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')
    image = models.ImageField(upload_to='images/productGallery',verbose_name='تصویر')


    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'تصویر گالری'
        verbose_name_plural = 'تصاویر گالری'
























