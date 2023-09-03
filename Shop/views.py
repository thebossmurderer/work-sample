# _______________________________________________________Library____________________________________________________________________________
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView , DetailView
from django.views.generic.base import TemplateView
from Shop.models import productCategory, productBrand , productVisit, productGallery
from .models import Product
from django.db.models import Count
from siteModule.models import siteBanner
from utils.convertor import groupList
from utils.httpServices import getClientIp

# _______________________________________________________Views Code____________________________________________________________________________


class mainPageView(ListView):
    template_name = 'productList.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(mainPageView, self).get_context_data()
        query = Product.objects.all()
        product: Product = query.order_by('-price').first()
        dbMaxPrice = product.price if product is not None else 0
        context['dbMaxPrice'] = dbMaxPrice
        context['startPrice'] = self.request.GET.get('startPrice') or 0
        context['endPrice'] = self.request.GET.get('endPrice') or dbMaxPrice
        context['banners'] = siteBanner.objects.filter(isActive=True,
                                                       position__iexact=siteBanner.siteBannerPositions.productList)
        return context

    def get_queryset(self):
        query = super(mainPageView, self).get_queryset()
        category = self.kwargs.get('cat')
        brands = self.kwargs.get('brand')
        request: HttpRequest = self.request
        startPrice = request.GET.get('startPrice')
        endPrice = request.GET.get('endPrice')
        if startPrice is not None:
            query = query.filter(price__gte=startPrice)
        if endPrice is not None:
            query = query.filter(price__lte=endPrice)
        if brands is not None:
            query = query.filter(brand__urlTitle__iexact=brands, isActive=True)
        if category is not None:
            query = query.filter(category__urlTitle__iexact=category, isActive=True)
        return query


class detailPageView(DetailView):
    template_name = 'productDetails.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # slug = kwargs['slug']
        loadedProduct = self.object
        # product = get_object_or_404(Product, slug=slug)
        # context['product'] = product
        context['banners'] = siteBanner.objects.filter(isActive=True,position__iexact=siteBanner.siteBannerPositions.productDetial)
        galleries = list(productGallery.objects.filter(product_id=loadedProduct.id).all())
        galleries.insert(0,loadedProduct)
        context['productGalleriesGroup'] = groupList(galleries,3)
        context['relatedProducts'] = groupList(list(Product.objects.filter(brand_id=loadedProduct.brand_id).exclude(pk=loadedProduct.id).all()[:6]),3)
        userIp = getClientIp(self.request)
        userId = None
        if self.request.user.is_authenticated:
            userId = self.request.user.id
        hasBeenVisited = productVisit.objects.filter(ip__iexact=userIp,product_id=loadedProduct.id).exists()
        if not hasBeenVisited:
            newVisit = productVisit(ip=userIp,user_id=userId,product_id=loadedProduct.id)
            newVisit.save()
        return context




def productCategoriesPartial(request: HttpRequest):
    productCtegories = productCategory.objects.filter(isActive=True, isDelete=False)
    context = {
        'categories': productCtegories
    }
    return render(request, 'includes/productCategoriesPartial.html', context)


def productBrandPartial(request: HttpRequest):
    productBrands = productBrand.objects.annotate(product_count=Count('product')).filter(isActive=True)
    context = {
        'brands': productBrands
    }
    return render(request, 'includes/productBrandPartial.html', context)
