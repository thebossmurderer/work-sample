from django.db.models import Count
from django.shortcuts import render
from django.views.generic.base import TemplateView
from siteModule.models import siteSetting, footerLink, footerLinksBox, slider
from utils.convertor import groupList
from Shop.models import Product, productCategory


# Create your views here.


class homeView(TemplateView):
    template_name = 'homeModule/indexPage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sliders = slider.objects.filter(isActive=True)
        context['sliders'] = sliders
        latestProducts = Product.objects.filter(isActive=True, isDelete=False).order_by('-id')[:8]
        mostVisitProducts = Product.objects.filter(isActive=True, isDelete=False).annotate(
            visitCount=Count('productvisit')).order_by('-visitCount')[:8]
        context['latestProducts'] = groupList(latestProducts)
        context['mostVisitProducts'] = groupList(mostVisitProducts)
        categories = list(productCategory.objects.annotate(productsCount=Count('product_categories')).filter(isActive=True,isDelete=False,productsCount__gt=0)[:6])
        categoriesProducts = []
        for category in categories:
            item = {
                'id': category.id,
                'title': category.title,
                'products': list(category.product_categories.all()[:4])
            }
            categoriesProducts.append(item)

        context['categoriesProducts'] = categoriesProducts

        return context


def siteHeaderPartial(request):
    settings: siteSetting = siteSetting.objects.filter(isMainSetting=True).first()
    context = {
        'siteSettings': settings
    }
    return render(request, 'shared/headerPartial.html', context)


def siteFooterPartial(request):
    settings: siteSetting = siteSetting.objects.filter(isMainSetting=True).first()
    footerLinkBox = footerLinksBox.objects.all()
    for item in footerLinkBox:
        item.footerlink_set
    context = {
        'siteSettings': settings,
        'footerLinkBox': footerLinkBox,
    }
    return render(request, 'shared/footerPartial.html', context)


class aboutView(TemplateView):
    template_name = 'homeModule/aboutPage.html'

    def get_context_data(self, **kwargs):
        context = super(aboutView, self).get_context_data(**kwargs)
        siteSettings: siteSetting = siteSetting.objects.filter(isMainSetting=True).first()
        context['siteSettings'] = siteSettings
        return context
