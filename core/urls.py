
from django.urls import path
from .import views

app_name='core'
urlpatterns = [
    path('', views.home, name='home'),            
    path('products/', views.products, name='products_page'),            
    path('checkout/', views.checkout, name='checkout_page'),            

    path('list/',views.item_list, name='item_list'),
]

