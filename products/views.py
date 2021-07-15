from django.conf import settings
from django.core.cache import cache
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.cache import cache_page

from products.models import Product, ProductCategory


def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.all()
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.all()


def get_products():
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.all().select_related('category')
            cache.set(key, products)
        return products
    else:
        return Product.objects.all().select_related('category')


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


@cache_page(3600)
def products(request, category_id=None, page=1):
    paginator = Paginator(Product.objects.filter(category_id=category_id) if category_id else get_products(), 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context = {'title': 'GeekShop - Каталог',
               'categories': get_links_menu(),
               'products': products_paginator}
    return render(request, 'products/products.html', context)
