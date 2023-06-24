from django.urls import path
from . import views

urlpatterns = [
    path("<int:product_id>/", views.get_product, name="product"),
    path("all/",views.get_all_products,name="products")
]