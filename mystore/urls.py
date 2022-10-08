from django.urls import path, include
from .views import ProductListView, ProductDetailView
from . import views


urlpatterns =[
    path('', views.ProductListView, name='store'),
    path('<int:pk>/', ProductDetailView.as_view(), name ='product_detail'),  
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem , name='update_item'),
    path('process_order/', views.processOrder , name='process_order')
]
