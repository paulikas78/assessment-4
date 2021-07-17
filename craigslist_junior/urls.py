from django.urls import path
from . import views

urlpatterns = [
    #  Categories URLs
    path('', views.categories, name='categories'),
    path('<int:category_id>', views.category_detail, name='category_detail'),
    path('new', views.new_category, name='new_category'),
    path('<int:category_id>/edit', views.category_edit, name='category_edit'),
    path('<int:category_id>/delete', views.category_delete, name='category_delete'),
    
    #  Posts URLs
    path('<int:category_id>/posts/<int:post_id>', views.post_detail, name='post_detail'),
    path('<int:category_id>/posts/new', views.new_post, name='new_post'),
    path('<int:category_id>/posts/<int:post_id>/edit', views.post_edit, name='post_edit'),
    path('<int:category_id>/posts/<int:post_id>/delete', views.post_delete, name='post_delete')
]