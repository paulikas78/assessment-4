from django.shortcuts import render, redirect
from .models import Category, Post
from .forms import CategoryForm, PostForm

def categories(request):
    all_categories = Category.objects.all()
    return render(request, 'categories.html', {'all_categories': all_categories})

def category_detail(request, category_id):
    category = Category.objects.get(id=category_id)
    return render(request, 'category_detail.html', {'category': category})

def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm()
    return render(request, 'category_form.html', {'form': form, 'type': 'New'})

def category_edit(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_detail', category_id=category.id)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_form.html', {'form': form, 'type': 'Edit'})

def category_delete(request, category_id):
    if request.method == 'POST':
        category = Category.objects.get(id=category_id)
        category.delete()
    return redirect('categories')

def post_detail(request, category_id, post_id):
    category = Category.objects.get(id=category_id)
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'category': category, 'post': post})

def new_post(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', category_id=category.id, post_id=post.id)
    else:
        form = PostForm(initial={'category': category})
    return render(request, 'post_form.html', {'form': form, 'type': 'New', 'category': category })

def post_edit(request, category_id, post_id):
    category = Category.objects.get(id=category_id)
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', category_id=category.id, post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form, 'type': 'Edit', 'category': category })

def post_delete(request, category_id, post_id):
    if request.method == 'POST':
        post = Post.objects.get(id=post_id)
        post.delete()
    return redirect('category_detail', category_id=category_id)


