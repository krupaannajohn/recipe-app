# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

def upload_recipe(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        ingredients = request.POST.get('ingredients')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        Recipe.objects.create(title=title, ingredients=ingredients, description=description, image=image)
        return redirect('index')
    return render(request, 'uploads.html')

def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        recipe.delete()
        return redirect('index')
    return render(request, 'delete_recipe.html', {'recipe': recipe})