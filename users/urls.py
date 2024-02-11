from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_all_users),
    path('users/<int:user_id>/', views.get_user_by_id),
    path('users/new/', views.create_user),
    path('users/<int:user_id>/update/', views.update_user),
    path('users/<int:user_id>/patch/', views.patch_user),
    path('users/<int:user_id>/delete/', views.delete_user),
]
