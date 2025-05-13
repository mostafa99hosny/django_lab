from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Category
from .forms import CategoryForm

# ViewSet for Category
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]

    def get_template_names(self):
        if self.action == 'list':
            return ['category/category_list.html']
        elif self.action == 'retrieve':
            return ['category/category_detail.html']
        elif self.action in ['create', 'update']:
            return ['category/category_form.html']
        return ['category/category_list.html']

    def get_success_url(self):
        return reverse_lazy('category:category_list')

# Function-based views for traditional Django rendering
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = category.products.all()
    return render(request, 'category/category_detail.html', {'category': category, 'products': products})

@login_required
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.success(request, 'Category created successfully!')
            return redirect('category:category_detail', pk=category.pk)
    else:
        form = CategoryForm()
    return render(request, 'category/category_form.html', {'form': form, 'title': 'Create Category'})

@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category updated successfully!')
            return redirect('category:category_detail', pk=category.pk)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category/category_form.html', {'form': form, 'category': category, 'title': 'Update Category'})

@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category deleted successfully!')
        return redirect('category:category_list')
    return render(request, 'category/category_confirm_delete.html', {'category': category})
