from django.shortcuts import render
from .models import Product

def home_view(request):
    featured_products = Product.objects.filter(visible=True)[:8]  # example query
    return render(request, 'core/home.html', {'featured_products': featured_products})

def product_list_view(request):
    # Add simple filter/search if you want or just show all
    products = Product.objects.filter(visible=True)
    categories = Product.objects.values_list('category', flat=True).distinct()
    return render(request, 'core/product_list.html', {
        'products': products,
        'categories': categories,
    })

def product_detail_view(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'core/product_detail.html', {'product': product})

def branches_view(request):
    from .models import Branch
    branches = Branch.objects.all()
    return render(request, 'core/branches.html', {'branches': branches})

def cart_view(request):
    # Your logic here
    return render(request, 'core/cart.html')
