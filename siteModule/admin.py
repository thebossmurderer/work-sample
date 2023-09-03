from django.contrib import admin
from . import models


# Register your models here.

class footerLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'footerLinkBox']


class sliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'url', 'isActive']
    list_editable = ['url', 'isActive']


class siteBannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'position']


admin.site.register(models.siteSetting)
admin.site.register(models.footerLinksBox)
admin.site.register(models.footerLink, footerLinkAdmin)
admin.site.register(models.slider, sliderAdmin)
admin.site.register(models.siteBanner, siteBannerAdmin)
