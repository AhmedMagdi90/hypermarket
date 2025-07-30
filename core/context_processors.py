from .models import MainCategory

def navbar_categories(request):
    return {
        'categories': MainCategory.objects.all()
    }
def common_counts(request):
    wishlist_count = 0
    cart_item_count = 0

    if request.user.is_authenticated:
        # Example: adjust according to your wishlist logic/model
        wishlist_count = request.user.wishlist_items.count()  # Replace with your actual relation/query

        # Example: adjust with how you handle cart
        cart_item_count = 0
        cart = request.session.get('cart', {})
        cart_item_count = sum(cart.values())  # Assuming a dict of product_id: quantity

    return {
        'wishlist_count': wishlist_count,
        'cart_item_count': cart_item_count,
    }
