from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'category'

# Set up the router for ViewSets
router = DefaultRouter()
router.register(r'', views.CategoryViewSet, basename='category')

urlpatterns = [
    # Function-based views
    path('list/', views.category_list, name='category_list'),
    path('<int:pk>/', views.category_detail, name='category_detail'),
    path('create/', views.category_create, name='category_create'),
    path('<int:pk>/update/', views.category_update, name='category_update'),
    path('<int:pk>/delete/', views.category_delete, name='category_delete'),
    
    # ViewSet API routes
    path('api/', include(router.urls)),
]
