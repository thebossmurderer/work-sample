from django.contrib import admin
from . import models


# Register your models here.

class productAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }

    list_display = ['title','price','information','rating','category']

admin.site.register(models.productCategory)
admin.site.register(models.Product,productAdmin)
admin.site.register(models.productInformation)
admin.site.register(models.productTags)
admin.site.register(models.productBrand)
admin.site.register(models.productVisit)
admin.site.register(models.productGallery)
