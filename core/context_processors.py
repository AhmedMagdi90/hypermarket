from .models import MainCategory

def navbar_categories(request):
    return {
        'categories': MainCategory.objects.all()
    }
