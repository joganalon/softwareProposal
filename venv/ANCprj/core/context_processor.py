from core.models import Product, Vendor, Category, FoodTray, OrderedProducts, Favourite, ProductImages, ProductReview, TableNum, FoodGroup
from django.db.models import Min, Max

def default(request):
    categories = Category.objects.all()
    vendors = Vendor.objects.all()

    min_max_price=Product.objects.aggregate(Min('price'),Max('price'))

    return {
        'categories': categories,
        'vendors':vendors,
        'min_max_price': min_max_price
    }