from django.contrib import admin
from .models import Branch, Product, Customer, Order, OrderItem , MainCategory, SubCategory 

admin.site.register(Branch)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_main_category', 'subcategory', 'price', 'visible')
    list_filter = ('subcategory', 'visible', 'subcategory__main_category')

    def get_main_category(self, obj):
        return obj.subcategory.main_category.name if obj.subcategory else '-'
    get_main_category.short_description = 'Main Category'
    get_main_category.admin_order_field = 'subcategory__main_category__name'



class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1

@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInline]
    list_display = ('name',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'main_category')
    list_filter = ('main_category',)