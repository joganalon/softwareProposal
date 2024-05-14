from django.urls import path
from core.views import index, category_list_view

app_name = 'core'

urlpatterns = [
    path('', index, name = 'index'), #the name is the one we will be passing to other functions
    path('category/', category_list_view, name='category-list')
]