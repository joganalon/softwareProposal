from django.shortcuts import render

from core.models import Product, Vendor, Category, FoodTray, OrderedProducts, Favourite, ProductImages, ProductReview, TableNum

def index(request):
    products = Product.objects.filter(product_status='published')

    context = {
        'products':products
    }

    return render(request, 'core/index.html', context)
