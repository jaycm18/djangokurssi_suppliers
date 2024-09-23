from django.urls import path

from .views import deletesupplier, productlistview, supplierlistview, deletesupplier, products_filtered
from .views import addsupplier, addproduct, deleteproduct, confirmdeleteproduct, confirmdeletesupplier
from .views import edit_product_post, edit_product_get, searchsuppliers, loginview, login_action, logout_action
from .views import carlistview, add_car, edit_car_get, edit_car_post, cars_by_supplier, delete_car, confirm_delete_car
from .views import customerlistview, add_customer, delete_customer, confirm_delete_customer

urlpatterns = [
    # Landing page after login
    #path('landing', landingview),

    # Loginview and authentication methods
    path('', loginview),
    path('login/', login_action),
    path('logout/', logout_action),

    # Products url´s
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post),
    path('products-by-supplier/<int:id>/', products_filtered),

    # Supplier url´s
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
    path('search-suppliers/', searchsuppliers),

    # Car url´s
    path('cars/', carlistview),
    path('add-car/', add_car),
    path('cars-by-supplier/<int:id>/', cars_by_supplier),
    path('edit-car/<int:id>/', edit_car_get),
    path('edit-car-post/<int:id>/', edit_car_post),
    path('delete-car/<int:id>/', delete_car),  
    path('confirm-delete-car/<int:id>/', confirm_delete_car),

    # Customer url´s
    path('customers/', customerlistview, name='customer_list'),
    path('add-customer/', add_customer),
    path('delete-customer/<int:id>/', delete_customer),
    path('confirm-delete-customer/<int:id>/', confirm_delete_customer),

]