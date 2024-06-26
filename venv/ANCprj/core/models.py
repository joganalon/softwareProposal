from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User
from taggit.managers import TaggableManager
from ckeditor_uploader.fields import RichTextUploadingField


STATUS_CHOICE = (
    ('received', 'Order Received'),
    ('process', 'Food Preparation Ongoing'),
    ('prepared', 'Ready for Pickup'),
    ('collected', 'Order Collected'),
)

STATUS = (
    ('draft', 'Draft'),
    ('disabled', 'Disabled'),
    ('rejected', 'Rejected'),
    ('in_review', 'In Review'),
    ('published', 'Published'),
)

RATING = (
    (1, '★☆☆☆☆'),
    (2, '★★☆☆☆'),
    (3, '★★★☆☆'),
    (4, '★★★★☆'),
    (5, '★★★★★'),
)
    

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class Category(models.Model):
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='cat', alphabet='abcdefgh12345')
    title = models.CharField(max_length=100, default='Meal')

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.title
    

class FoodGroup(models.Model):
    fid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='foo', alphabet='abcdefgh12345')
    title = models.CharField(max_length=100, default='Type of Food')
    
    class Meta:
        verbose_name_plural = 'Food Groups'
    
    def __str__(self):
        return self.title

#class Tags(models.Model):
 #   pass
    

class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='ven', alphabet='abcdefgh12345')

    title = models.CharField(max_length=100, default='Vendor')
    image = models.ImageField(upload_to=user_directory_path, default='vendor.jpg')
    description = RichTextUploadingField(null=True, blank=True, default='We are an amazing vendor.')

    address = models.CharField(max_length=100, default='Ateneo')
    contact = models.CharField(max_length=100, default='09091234567')
    chat_resp_time = models.CharField(max_length=100, default='100')
    authentic_rating = models.CharField(max_length=100, default='100')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Vendors'

    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    

class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='prd', alphabet='abcdefgh12345')

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')
    foodgroup = models.ForeignKey(FoodGroup, on_delete=models.SET_NULL, null=True, related_name='foodgroup')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, related_name='product')

    title = models.CharField(max_length=100, default='Product.')
    image = models.ImageField(upload_to='category', default='product.jpg')
    description = RichTextUploadingField(null=True, blank=True, default='Order now.')

    price = models.DecimalField(max_digits=999, decimal_places=2, default='49.99')
    old_price = models.DecimalField(max_digits=999, decimal_places=2, default='59.99')

    ingredients = RichTextUploadingField(null=True, blank=True)

    tags = TaggableManager(blank=True)

    product_status = models.CharField(choices=STATUS, max_length=15, default='in_review')

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    
    sku = ShortUUIDField(unique=True, length=4, max_length=10, prefix='sku', alphabet='1234567890')

    date = models.DateTimeField(auto_now_add=True)
    updates = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Products'

    def product_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    
    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price

class ProductImages(models.Model):
    images = models.ImageField(upload_to='product-images', default='product.jpg')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product_images')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Images'

######################## Cart, Order, OrderItems ##########

class FoodTray(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=999, decimal_places=2, default='49.99')
    payment_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default='received')

    class Meta:
        verbose_name_plural = 'Food Trays'

class OrderedProducts(models.Model):
    order = models.ForeignKey(FoodTray, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=999, decimal_places=2, default='49.99')
    total = models.DecimalField(max_digits=999, decimal_places=2, default='49.99')

    class Meta:
        verbose_name_plural = 'Food Orders'

    def order_image(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))
    

    ######################### Product review, favourites, address #######################

class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='reviews')
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Product Reviews'

    def __str__(self):
        return self.product.title
        
    def get_rating(self):
        return self.ratings
        
class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Favourites'

    def __str__(self):
        return self.product.title
        
class TableNum(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tableNum = models.IntegerField(null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Table Numbers'