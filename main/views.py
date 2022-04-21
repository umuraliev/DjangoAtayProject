from django.shortcuts import render
from main.models import Category, Product

def all_product(request):
    products = Product.objects.all()
    return render(request, 'product.html', locals())
    
def all_category(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})