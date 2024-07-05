from django.shortcuts import render
from .models import Recipe, Step
from django.db.models import Q


# Create your views here.
def home(request):
    content = request.GET.get('q')
    if content:
        recipes = Recipe.objects.filter(Q(title__icontains=content))
    else:
        recipes = Recipe.objects.all()

    recentRecipies = Recipe.objects.all().order_by('-createdAt')

    context = {'all_recipes' :recipes, 'recent_Recipies': recentRecipies}


    return render(request ,'base/home.html', context)

def cook(request, pk):
    recipes = Recipe.objects.get(id=pk)
    steps = Step.objects.filter(recipe = recipes)
    context = {'Recipe': recipes, 'Steps': steps}

    return render(request, 'base/cook.html', context)