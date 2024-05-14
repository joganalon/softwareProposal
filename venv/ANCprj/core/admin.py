from django.contrib import admin
from core.models import Product, Vendor, Category, FoodTray, OrderedProducts, Favourite, ProductImages, ProductReview, TableNum

class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['user', 'title', 'product_image', 'category', 'vendor', 'price', 'featured', 'product_status']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category_image']

class VendorAdmin(admin.ModelAdmin):
    list_display = ['title', 'vendor_image']

class FoodTrayAdmin(admin.ModelAdmin):
    list_display = ['user', 'price', 'payment_status', 'order_date', 'product_status']

class OrderedProductsAdmin(admin.ModelAdmin):
    list_display = ['order', 'invoice_no', 'item', 'image', 'qty', 'price', 'total']      

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'rating'] 

class FavouriteAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'date'] 

class TableNumAdmin(admin.ModelAdmin):
    list_display = ['user', 'tableNum', 'status'] 


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(FoodTray, FoodTrayAdmin)
admin.site.register(OrderedProducts, OrderedProductsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(Favourite, FavouriteAdmin)
admin.site.register(TableNum, TableNumAdmin)