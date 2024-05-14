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