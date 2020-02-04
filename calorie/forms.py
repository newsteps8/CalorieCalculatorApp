from django import forms
from .models import Calorie
from .models import Meal



class CalorieForm(forms.ModelForm):


    class Meta:
        model = Calorie
        fields = [
            'Gender',
            'Activity',
            'Age',
            'Height',
            'Weight',

        ]


class  MealForm(forms.ModelForm):


    class Meta:
        model = Meal
        fields = [
            'Food',
            'Amount',

        ]