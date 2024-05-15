from django.shortcuts import render

from core.models import Product, Vendor, Category, FoodTray, OrderedProducts, Favourite, ProductImages, ProductReview, TableNum

def index(request):
    products = Product.objects.all()

    context = {
        'products':products
    }

    return render(request, 'core/index.html', context)

def category_list_view(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'core/category-list.html', context)

def product_list_category_view(request, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(product_status='published', category=category)

    context = {
        'category':category,
        'products':products,
    }

    return render(request, 'core/category-product-list.html')