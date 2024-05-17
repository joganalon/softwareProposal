from django.urls import path
from core.views import index, foodGroup_list_view, product_list_foodGroup_view, category_list_view, product_list_category_view, vendor_list_view, vendor_detail, product_detail_view, ajax_add_review, search_view, filter_product #tag_list

app_name = 'core'

urlpatterns = [
    path('', index, name = 'index'), #the name is the one we will be passing to other functions
    path('products/<pid>/', product_detail_view, name='product-detail'),

    #category
    path('category/', category_list_view, name='category-list'),
    path('category/<cid>/', product_list_category_view, name='category-product-list'),

    #foodgroup
    path('food-group/', foodGroup_list_view, name='food-group-list'),
    path('food-group/<fid>/', product_list_foodGroup_view, name='food-group-product-list'),

    #vendor
    path('vendor/', vendor_list_view, name='vendor-list'),
    path('vendor/<vid>/', vendor_detail, name='vendor-detail'),

    #tags
    #path('products/tags/<slug:tag_slug/>', tag_list, name='tags'),

    #add review
    path('ajax-add-review/<int:pid>/', ajax_add_review, name='ajax-add-review'),

    #search
    path('search/', search_view, name='search'),

    path('filter-products/', filter_product, name='filter-product')

]