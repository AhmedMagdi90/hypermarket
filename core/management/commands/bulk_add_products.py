from django.core.management.base import BaseCommand
from core.models import Product, SubCategory

class Command(BaseCommand):
    help = 'Bulk add example products for testing'

    def handle(self, *args, **options):
        # Prepare your subcategories; adjust names as needed to match your DB!
        subcat_map = { 
            s.name: s for s in SubCategory.objects.all()
        }

        # Example bulk product data
        test_products = [
            {'name': 'Banana', 'price': 10, 'subcategory': 'Vegetables & Fruits', 'visible': True},
            {'name': 'Apple Juice', 'price': 20, 'subcategory': 'Juices', 'visible': True},
            {'name': 'Whole Wheat Bread', 'price': 15, 'subcategory': 'Bakery', 'visible': True},
            {'name': 'Laundry Detergent', 'price': 50, 'subcategory': 'Cleaning Supplies', 'visible': True},
            {'name': 'Baby Formula', 'price': 100, 'subcategory': 'Baby Food', 'visible': True},
            {'name': 'Headphones', 'price': 200, 'subcategory': 'TV & Audio', 'visible': True},
            {'name': 'Football', 'price': 70, 'subcategory': 'Sportswear', 'visible': True},
            {'name': 'Pet Leash', 'price': 25, 'subcategory': 'Accessories', 'visible': True},
        ]

        created = 0
        for pdata in test_products:
            subcat = subcat_map.get(pdata['subcategory'])
            if not subcat:
                self.stdout.write(self.style.WARNING(f"SubCategory not found: {pdata['subcategory']} (Skipping {pdata['name']})"))
                continue
            product, was_created = Product.objects.get_or_create(
                name=pdata['name'],
                defaults={
                    'price': pdata['price'],
                    'subcategory': subcat,
                    'visible': pdata['visible'],
                }
            )
            if was_created:
                created += 1
                self.stdout.write(self.style.SUCCESS(f"Created: {product.name}"))
            else:
                self.stdout.write(f"Already exists: {product.name}")

        self.stdout.write(self.style.SUCCESS(f"{created} products created!"))
