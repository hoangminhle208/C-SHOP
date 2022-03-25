from django.contrib import admin
from .models.product import Product
from .models.category import Category
# Register your models here.


# CHIEN: hiện thị thông tin sản phẩm để admin dễ thao tác
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'thuonghieu']
# CHIEN: hiển thị thông tin của danh mục sản phẩm
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

# CHIEN: tạo site Product cho admin
admin.site.register(Product, AdminProduct)

# CHIEN: tạo site Category cho admin
admin.site.register(Category, AdminCategory)
