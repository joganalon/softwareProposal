from core.models import Product, Vendor, Category, FoodTray, OrderedProducts, Favourite, ProductImages, ProductReview, TableNum

def default(request):
    categories = Category.objects.all()
    return {
        'categories': categories,
    }