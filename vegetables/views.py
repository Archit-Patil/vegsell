from django.shortcuts import render
from .models.product import Product
from .models.category import Category

def home(request):
    products = Product.get_all_products()
    return render(request, 'vegetables/home.html',{'products':products})

def about(request):
    return render(request, 'vegetables/about.html')

def shopping(request):
    products = None

    categorys = Category.get_all_categories()
    categoryid = request.GET.get('category')

    if categoryid:
        products = Product.get_all_categories_by_id(categoryid)

    else:
        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['categorys'] = categorys
    return render(request, 'vegetables/shopping.html',data)


def productdetail(request,id):
    products = Product.objects.get(id=id)
    data = {}
    data['products'] = products
    return render(request, 'vegetables/productdetail.html',data)
