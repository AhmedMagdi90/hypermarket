from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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
    # Example placeholder: Replace with actual cart retrieval logic
    cart_items = []  # your cart items queryset or session data here
    cart_total = 0
    return render(request, 'core/cart.html', {'cart_items': cart_items, 'cart_total': cart_total})

def remove_from_cart_view(request, item_id):
    if request.method == 'POST':
        # Add your logic to remove the cart item by id
        # Example:
        # item = get_object_or_404(CartItem, id=item_id)
        # item.delete()
        pass
    return redirect('cart')

def checkout_view(request):
    # Your checkout logic or a simple placeholder page
    return render(request, 'core/checkout.html')

def product_list_view(request):
    products = Product.objects.filter(visible=True)

    # Get filter/search params from query string
    q = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()

    if q:
        products = products.filter(name__icontains=q)

    if category:
        products = products.filter(category=category)

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 12)  # 12 products per page

    try:
        products_page = paginator.page(page)
    except PageNotAnInteger:
        products_page = paginator.page(1)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)

    # Unique categories list for filter dropdown (or sidebar)
    categories = Product.objects.values_list('category', flat=True).distinct()

    context = {
        'products': products_page,
        'categories': categories,
        'query': q,
        'selected_category': category,
        'paginator': paginator,
        'page_obj': products_page,
    }
    return render(request, 'core/product_list.html', context)