from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('view-cart/', views.view_cart, name='view_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:item_id>/<str:action>/', views.update_quantity, name='update_quantity'),
    path('signup/', views.signup_view, name='signup_view'),
    path('', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('checkout/', views.checkout_view, name='checkout'),


]
