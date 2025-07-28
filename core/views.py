from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from core.models import Product, MainCategory, Branch, UserProfile
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import UsernameOrPhoneLoginForm
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserEditForm, UserProfileForm, UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import login


def home_view(request):
    featured_products = Product.objects.filter(visible=True)[:8]
    categories = MainCategory.objects.all()
    return render(request, 'core/home.html', {
        'featured_products': featured_products,
        'categories': categories,
    })


def product_list_view(request):
    products = Product.objects.filter(visible=True).order_by('id')
    q = request.GET.get('q', '').strip()
    category_id = request.GET.get('category', '').strip()
    if category_id:
        try:
            category_id_int = int(category_id)
            products = products.filter(subcategory__main_category__id=category_id_int)
        except ValueError:
            products = products.none()

    page = request.GET.get('page', 1)
    paginator = Paginator(products, 12)
    try:
        products_page = paginator.page(page)
    except PageNotAnInteger:
        products_page = paginator.page(1)
    except EmptyPage:
        products_page = paginator.page(paginator.num_pages)

    categories = MainCategory.objects.all()

    context = {
        'products': products_page,
        'categories': categories,
        'query': q,
        'selected_category': category_id,
        'paginator': paginator,
        'page_obj': products_page,
    }
    return render(request, 'core/product_list.html', context)


def branches_view(request):
    branches = Branch.objects.all()
    return render(request, 'core/branches.html', {'branches': branches})


def cart_view(request):
    cart_items = []  # Your logic here
    cart_total = 0
    return render(request, 'core/cart.html', {'cart_items': cart_items, 'cart_total': cart_total})


def remove_from_cart_view(request, item_id):
    if request.method == 'POST':
        # Implement removal logic here
        pass
    return redirect('cart')


def checkout_view(request):
    return render(request, 'core/checkout.html')


def product_detail_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'core/product_detail.html', {'product': product})


@require_POST
def cart_add_view(request, product_id):
    # Implement cart add logic here
    return redirect('product_detail', product_id=product_id)


@require_POST
def wishlist_toggle_view(request, product_id):
    # Implement wishlist toggle logic here
    return redirect('product_detail', product_id=product_id)


@login_required
def account_profile_view(request):
    return render(request, "core/account_profile.html")


class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    authentication_form = UsernameOrPhoneLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or '/'


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            # Save profile info
            UserProfile.objects.create(
                user=new_user,
                full_name=form.cleaned_data['full_name'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address']
            )
            login(request, new_user)
            messages.success(request, "Registration successful! Welcome to Hyper Market.")
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def profile_edit_view(request):
    user = request.user
    try:
        profile = user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile(user=user)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your profile has been updated.")
            return redirect('account_profile')
    else:
        user_form = UserEditForm(instance=user)
        profile_form = UserProfileForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'core/profile_edit.html', context)