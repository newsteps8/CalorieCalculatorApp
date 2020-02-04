from django.contrib import admin
from .models import Calorie
from .models import Meal


class CalorieAdmin(admin.ModelAdmin):
    list_display = ['Gender', 'publishing_date', 'slug']
    list_display_links = ['publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['Gender','Activity','Age','Weight','Height','calc']
    list_editable = ['Gender']

    class Meta:
        model = Calorie



admin.site.register(Calorie, CalorieAdmin)


class  MealAdmin(admin.ModelAdmin):
    list_display = ['Food', 'publishing_date', 'slug']
    list_display_links = ['publishing_date']
    list_filter = ['publishing_date']
    search_fields = ['Food', 'Amount','new_calorie','remain_Cal','calc','key']
    list_editable = ['Food']

    class Meta:
        model = Meal



admin.site.register(Meal, MealAdmin)