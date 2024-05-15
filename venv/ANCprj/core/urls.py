from django.urls import path
from core.views import index, category_list_view, product_list_category_view, vendor_list_view

app_name = 'core'

urlpatterns = [
    path('', index, name = 'index'), #the name is the one we will be passing to other functions

    #category
    path('category/', category_list_view, name='category-list'),
    path('category/<cid>/', product_list_category_view, name='category-product-list'),

    #vendor
    path('vendor/', vendor_list_view, name='vendor-list')

]