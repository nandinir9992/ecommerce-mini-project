from django.contrib import admin
from .models import Product, Cart, CartItem, Order, ShippingAddress

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'status')

class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('order', 'address', 'city', 'postal_code', 'country')

admin.site.register(ShippingAddress, ShippingAddressAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category')
    search_fields = ('name', 'category')
    list_filter = ('category',)
admin.site.register(Product, ProductAdmin)


admin.site.register(Order, OrderAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)

