from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    # Class-based views (Generic)
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('create/', views.ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', views.ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    
    # Function-based views
    path('fbv/', views.product_list, name='fbv_product_list'),
    path('fbv/<int:pk>/', views.product_detail, name='fbv_product_detail'),
    path('fbv/create/', views.product_create, name='fbv_product_create'),
    path('fbv/<int:pk>/update/', views.product_update, name='fbv_product_update'),
    path('fbv/<int:pk>/delete/', views.product_delete, name='fbv_product_delete'),
]
