from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_recipe, name='upload'),
    path('delete/<int:recipe_id>/', views.delete_recipe, name='delete_recipe'),
]