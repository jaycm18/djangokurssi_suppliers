from django.urls import path

from .views import deletesupplier, productlistview, supplierlistview, deletesupplier, products_filtered
from .views import addsupplier, addproduct, deleteproduct, confirmdeleteproduct, confirmdeletesupplier
from .views import edit_product_post, edit_product_get, searchsuppliers, loginview, login_action, logout_action

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
]