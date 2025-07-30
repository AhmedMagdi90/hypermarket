from django.urls import path
from . import views
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from .views import CustomLoginView  # if you have this custom view

urlpatterns = [
    path('', views.home_view, name='home'),
    path('products/', views.product_list_view, name='products'),
    path('products/<int:product_id>/', views.product_detail_view, name='product_detail'),

    path('branches/', views.branches_view, name='branches'),
    path('cart/', views.cart_view, name='cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart_view, name='remove_from_cart'),
    path('checkout/', views.checkout_view, name='checkout'),

    path('cart/add/<int:product_id>/', views.cart_add_view, name='cart_add'),
    path('wishlist/toggle/<int:product_id>/', views.wishlist_toggle_view, name='wishlist_toggle'),

    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),  # or use LoginView if no custom

    path('password_reset/', PasswordResetView.as_view(template_name='core/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='core/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'), name='password_reset_complete'),

    path('account/profile/', views.account_profile_view, name='account_profile'),
    path('account/profile/edit/', views.profile_edit_view, name='profile_edit'),

    path('register/', views.register_view, name='register'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
    path('wishlist/toggle/<int:product_id>/', views.wishlist_toggle_view, name='wishlist_toggle'),
]
