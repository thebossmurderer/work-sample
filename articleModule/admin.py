from django.contrib import admin
from django.http import HttpRequest
from . import models
from articleModule.models import article , articleComment

# Register your models here.

class articleCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'urlTitle', 'parent', 'isActive']
    list_editable = ['parent', 'isActive']

class articleAdmin(admin.ModelAdmin):
    list_display = ['title','slug','isActive','author']
    list_editable = ['isActive']


    def save_model(self, request :HttpRequest, obj:article, form, change):
        # if not change:
        obj.author = request.user
        return super().save_model(request,obj,form,change)


class articleCommentsAdmin(admin.ModelAdmin):
    list_display = ['user','createDate','parent']



admin.site.register(models.articleCategories, articleCategoryAdmin)
admin.site.register(models.article,articleAdmin)
admin.site.register(models.articleComment,articleCommentsAdmin)
