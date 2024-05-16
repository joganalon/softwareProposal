from django.shortcuts import render, get_object_or_404
from core.models import Product, Vendor, Category, FoodTray, OrderedProducts, Favourite, ProductImages, ProductReview, TableNum
from taggit.models import Tag
from django.db.models import Avg
from core.forms import ProductReviewForm

def index(request):
    products = Product.objects.all()
    context = {
        'products':products,
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

def vendor_list_view(request):
    vendors = Vendor.objects.all()
    context = {
        'vendors': vendors,
    }
    return render(request, 'core/vendor-list.html', context)

def vendor_detail(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(vendor=vendor, product_status='published')
    context = {
        'vendor': vendor,
        'products': products,
    }
    return render(request, 'core/vendor-detail.html', context)

def product_detail_view(request, pid):
    product = Product.objects.get(pid=pid)
    product_images = product.product_images.all()
    products = Product.objects.filter(category=product.category).exclude(pid=pid)
    reviews = ProductReview.objects.filter(product=product).order_by('-date')
    average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))
    review_form = ProductReviewForm()
    context = {
        'product':product,
        'product_images':product_images,
        'products':products,
        'reviews':reviews,
        'average_rating': average_rating,
        'review_form': review_form
    }
    return render(request, 'core/product-detail.html', context)

#def tag_list(request, tag_slug=None):
    products=Product.objects.filter(product_status='published').order_by('-id')
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        products=products.filter(tags__in=[tag])
    context={
        'products':products,
        'tag':tag
    }
    return render(request, 'core/tag.html', context)

def ajax_add_review(request, pid):
    product = Product.objects.get(pk=pid)
    user = request.user

    review = ProductReview.objects.create(
        user=user,
        product=product,
        review=request.POST['review'],
        rating=request.POST['rating']
    )

    context={
        'user': user.username,
        'review':request.POST['review'],
        'rating':request.POST['rating']
    }

    average_reviews = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    return JsonResponse({
        'bool': True,
        'context': context,
        'average_reviews':average_reviews
    })

def search_view(request):
    query = request.GET.get('q')

    products=Product.objects.filter(title__icontains=query, description__icontains=query).ordery_by('-date')
    context = {
        'products': products,
        'query':query
    }
    return render(request, 'core/search.html', context)