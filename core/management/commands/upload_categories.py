from django.core.management.base import BaseCommand
from core.models import MainCategory, SubCategory

class Command(BaseCommand):
    help = 'Bulk upload Main Categories and Subcategories'

    def handle(self, *args, **options):
        categories = {
            'Fresh Food': ['Vegetables & Fruits', 'Bakery', 'Dairy & Eggs', 'Meat & Fish'],
            'Beverages': ['Soft Drinks', 'Juices', 'Water'],
            'Household': ['Cleaning Supplies', 'Laundry', 'Kitchen Essentials'],
            'Beauty & Personal Care': ['Skin Care', 'Hair Care', 'Oral Care'],
            'Baby & Kids': ['Diapers', 'Baby Food', 'Toys'],
            'Electronics': ['Mobile Phones', 'Computers', 'TV & Audio'],
            'Clothing & Accessories': ['Men', 'Women', 'Children'],
            'Stationery & Books': ['Office Supplies', 'School Supplies', 'Books'],
            'Sports & Outdoors': ['Exercise Equipment', 'Outdoor Gear', 'Sportswear'],
            'Pet Supplies': ['Pet Food', 'Accessories', 'Healthcare'],
        }

        self.stdout.write('Starting to create Main Categories and SubCategories...')

        for main_cat_name, subcat_list in categories.items():
            main_cat, created_main = MainCategory.objects.get_or_create(name=main_cat_name)
            if created_main:
                self.stdout.write(self.style.SUCCESS(f'Created MainCategory: {main_cat_name}'))
            else:
                self.stdout.write(f'MainCategory already exists: {main_cat_name}')

            for subcat_name in subcat_list:
                subcat, created_sub = SubCategory.objects.get_or_create(name=subcat_name, main_category=main_cat)
                if created_sub:
                    self.stdout.write(self.style.SUCCESS(f'  Created SubCategory: {main_cat_name} -> {subcat_name}'))
                else:
                    self.stdout.write(f'  SubCategory already exists: {main_cat_name} -> {subcat_name}')

        self.stdout.write(self.style.SUCCESS('Finished creating categories.'))
