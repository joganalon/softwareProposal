from django.urls import path
from core.views import index, category_list_view, product_list_category_view

app_name = 'core'

urlpatterns = [
    path('', index, name = 'index'), #the name is the one we will be passing to other functions
    path('category/', category_list_view, name='category-list'),
    path('category/<cid>/', product_list_category_view, name='category-product-list')
]