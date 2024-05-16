from core.models import Product, Vendor, Category, FoodTray, OrderedProducts, Favourite, ProductImages, ProductReview, TableNum

def default(request):
    categories = Category.objects.all()
    #address=TableNum.objects.get(user=request.user))
    return {
        'categories': categories,
    }