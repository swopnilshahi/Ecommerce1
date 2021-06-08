from django.shortcuts import render
from .models import Item
# Create your views here.

def item_list(request):
    items =Item.objects.all()
    context = {
        'items': items,
    }
    return render(request,'core/item_list.html',context)

def home(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request,'core/home_page.html',context )

def products(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }

    return render(request,'core/product_page.html',context )

def checkout(request):
    return render(request,'core/checkout_page.html' )