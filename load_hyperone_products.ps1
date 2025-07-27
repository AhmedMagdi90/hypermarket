# Activate your virtual environment first
# .\.venv\Scripts\Activate.ps1

# Run python shell with script commands inside
python manage.py shell -c @"
from core.models import Product

# Define Hyperone-like categories and subcategories (flat strings here)
categories = {
    'Fresh Food / Groceries': ['Vegetables & Fruits', 'Bakery', 'Dairy & Eggs', 'Meat & Fish'],
    'Beverages': ['Soft Drinks', 'Juices', 'Water'],
    'Household': ['Cleaning Supplies', 'Laundry', 'Kitchen'],
    'Beauty & Personal Care': ['Skin Care', 'Hair Care', 'Oral Care'],
    'Baby & Kids': ['Diapers', 'Baby Food', 'Toys'],
    'Electronics': ['Mobile Phones', 'Computers', 'TV & Audio'],
    'Clothing & Accessories': ['Men', 'Women', 'Children'],
    'Stationery & Books': ['Office Supplies', 'School Supplies', 'Books'],
    'Sports & Outdoors': ['Exercise Equipment', 'Outdoor Gear', 'Sportswear'],
    'Pet Supplies': ['Pet Food', 'Accessories', 'Healthcare'],
}

# Sample products to add for each subcategory (for demo purpose)
sample_products = [
    {'name': 'Sample Tomato', 'description': 'Fresh ripe tomatoes.', 'price': 12.5},
    {'name': 'Whole Wheat Bread', 'description': 'Healthy bread.', 'price': 7.0},
    {'name': 'Fresh Milk', 'description': 'Dairy fresh milk.', 'price': 10.0},
    {'name': 'Chicken Breast', 'description': 'Boneless skinless chicken.', 'price': 25.0},
    {'name': 'Coca Cola 1L', 'description': 'Popular soft drink.', 'price': 8.5},
]

# Create products under each subcategory in categories
count = 1
for main_cat, subcats in categories.items():
    for subcat in subcats:
        # For demo, add 2 products per subcategory
        for i in range(2):
            prod_data = sample_products[(count - 1) % len(sample_products)]
            product_name = f"{prod_data['name']} {count}"
            description = prod_data['description']
            price = prod_data['price']
            
            p, created = Product.objects.get_or_create(
                name=product_name,
                defaults={
                    'description': description,
                    'price': price,
                    'category': subcat,
                    'visible': True,
                }
            )
            if created:
                print(f"Added product: {product_name} in category {subcat}")
            else:
                print(f"Product {product_name} already exists.")
            count += 1

print('Finished adding demo products with hyperone-like categories.')

"@
