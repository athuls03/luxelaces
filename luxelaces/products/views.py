from django.shortcuts import render
from . admin import Product
from django.core.paginator import Paginator
from random import shuffle

# Create your views here.

def index(request):
    featured_products=Product.objects.order_by('priority')[:4]
    latest_products=Product.objects.order_by('-id')[:4]
    context={
        "featured_products":featured_products,
        "latest_products":latest_products
    }
    return render(request,'index.html',context)

# def index(request):
#     all_products = Product.objects.all()
#     shuffled_products = list(all_products) 
#     shuffle(shuffled_products) 

#     featured_products = shuffled_products[:4]
#     latest_products = shuffled_products[4:8]  # Assuming you want 4 latest products as well

#     context = {
#         "featured_products": featured_products,
#         "latest_products": latest_products
#     }
#     return render(request, 'index.html', context)

def list_products(request):
    """_summary_
    returns products list page
    Args:
    request(_type_):_description_

    Returns:
    _type_:_description_

    """
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=Product.objects.order_by('-priority')
    product_paginator=Paginator(product_list,2)
    product_list=product_paginator.get_page(page)
    context={'products':product_list}
    return render(request,'products.html',context)

def detail_product(request,pk):
    product=Product.objects.get(pk=pk)
    context={'product':product}
    return render(request,'product_detail.html',context)
