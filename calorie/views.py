from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .forms import CalorieForm,MealForm
from .models import Calorie
from .models import Meal
from django.contrib import messages





def calorie_detail(request):#add slug parameter
    calorie = Calorie.objects.filter(user=request.user).order_by('id').last()
    form = CalorieForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.calorie = calorie
        comment.save()
        return HttpResponseRedirect(calorie.get_absolute_url)

    context = {
        'calorie': calorie,
        'form': form
    }
    return render(request, "calorie/detail.html", context)


def calorie_create(request):


    form = CalorieForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        calorie = form.save(commit=False)
        calorie.user = request.user
        calorie.save()
        messages.success(request, "You have successfully created it.", extra_tags='mesaj-basarili')
        return HttpResponseRedirect(calorie.get_absolute_url())



    context = {
        'form': form
    }

    return render(request, "calorie/form.html", context)

def result_detail(request):#add slug parameter
    meal = Meal.objects.filter(user=request.user).order_by('id').last()
    calorie = Calorie.objects.filter(user=request.user).order_by('id').last()
    form = MealForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.meal = meal
        comment.save()
        return HttpResponseRedirect(meal.get_absolute_url)

    context = {
        'meal': meal,
        'form': form,
        'calorie':calorie,
    }
    return render(request, "calorie/detail2.html", context)


def mealcalorie(request):


    form = MealForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        meal= form.save(commit=False)
        meal.user = request.user
        meal.save()
        messages.success(request, "You have successfully created it.", extra_tags='mesaj-basarili')
        return HttpResponseRedirect(meal.get_absolute_url())



    context = {
        'form': form
    }

    return render(request, "calorie/form2.html", context)




