from django.db import models
from django.urls import reverse
from django.utils.text import slugify
import requests

class Calorie(models.Model):
    user = models.ForeignKey('auth.User', related_name='calories',on_delete=models.CASCADE)
    Activity_1 = 'If you have a desk and a stationary life'
    Activity_2 = 'If you are slightly mobile'
    Activity_3 = 'If you are moderately active and do not sit very much'
    Activity_4 = 'If you are highly active and do regular sports'
    ACTIVITY_CHOICES = (
        (Activity_1, 'If you have a desk and a stationary life'),
        (Activity_2, 'If you are slightly mobile'),
        (Activity_3, 'If you are moderately active and do not sit very much'),
        (Activity_4, 'If you are highly active and do regular sports'),
    )
    Male = 'M'
    FeMale = 'F'
    GENDER_CHOICES = (
        (Male, 'Male'),
        (FeMale, 'Female'),
    )
    Activity = models.CharField(max_length = 200, choices = ACTIVITY_CHOICES,
                              default = 'Choose your daily activity')
    Gender = models.CharField(max_length = 6, choices = GENDER_CHOICES,
                              default = Male)
    Age = models.IntegerField()
    Height = models.IntegerField(verbose_name='Height - type in cm')
    Weight = models.IntegerField(verbose_name='Weight - type in kg')
    publishing_date = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    calc = models.FloatField(null=True)
    slug = models.SlugField(null=True, editable=False, max_length=130)




    @property
    def calorie_calc(self):


        if self.Gender == 'M':
            if self.Activity == 'If you have a desk and a stationary life':
                x = (66 + ((13.7) * self.Weight) + (5 * self.Height) - ((6.8) * self.Age)) * 1.2
            elif self.Activity == 'If you are slightly mobile':
                x = (66 + ((13.7) * self.Weight) + (5 * self.Height) - ((6.8) * self.Age)) * 1.3
            elif self.Activity == 'If you are moderately active and do not sit very much':
                x = (66 + ((13.7) * self.Weight) + (5 * self.Height) - ((6.8) * self.Age)) * 1.4
            elif self.Activity == 'If you are highly active and do regular sports':
                x = (66 + ((13.7) * self.Weight) + (5 * self.Height) - ((6.8) * self.Age)) * 1.5
        elif self.Gender == 'F':
            if self.Activity == 'If you have a desk and a stationary life':
                x = 655 + ((9.6)*self.Weight) + ((1.8)*self.Height) - ((4.7)*self.Age) * 1.2
            elif self.Activity == 'If you are slightly mobile':
                x = 655 + ((9.6)*self.Weight) + ((1.8)*self.Height) - ((4.7)*self.Age) * 1.3
            elif self.Activity == 'If you are moderately active and do not sit very much':
                x = 655 + ((9.6)*self.Weight) + ((1.8)*self.Height) - ((4.7)*self.Age) * 1.4
            elif self.Activity == 'If you are highly active and do regular sports':
                x = 655 + ((9.6)*self.Weight) + ((1.8)*self.Height) - ((4.7)*self.Age) * 1.5

        return round(x,2)




    def save(self, *args, **kwargs):

        self.calc = self.calorie_calc
        super(Calorie, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('calorie:detail')




class Meal(models.Model):
    user = models.ForeignKey('auth.User', related_name='meals', on_delete=models.CASCADE)
    Food = models.CharField(max_length=120, verbose_name='Food - ex: broccoli')
    Amount = models.IntegerField(verbose_name='Amount - type in gram or milliliter')
    publishing_date = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    new_Cal = models.FloatField(null=True)
    remain_Cal = models.FloatField(null=True)
    slug = models.SlugField(null=True, editable=False, max_length=130)
    key = models.ForeignKey('Calorie',null=True, on_delete=models.CASCADE)
    calc = models.FloatField(null=True)
    API_KEY = models.CharField(max_length=120)
    search_query = models.CharField(max_length=120)

    class Meta:
        ordering = ['-publishing_date', 'id']

    @property
    def meal_calc(self):
        first_url = "https://api.nal.usda.gov/fdc/v1/search?api_key=" + "2IEEIUW3ZUNfev9I3ltPS2nGvbVoBZz2sURdrsdx" + "&generalSearchInput=" + self.Food
        json_data = requests.get(first_url).json()
        fdcId = json_data['foods'][0]['fdcId']
        second_url = second_url = "https://api.nal.usda.gov/fdc/v1/" + str(
            fdcId) + "?api_key=" + "2IEEIUW3ZUNfev9I3ltPS2nGvbVoBZz2sURdrsdx"
        json_data = requests.get(second_url).json()
        x = json_data['labelNutrients']['calories']['value']
        return round(x / 100 * self.Amount,2) # amount of food is taken from the website that have 100 gr

    def save(self, *args, **kwargs):
        another_model = Calorie.objects.last()
        self.calc = another_model.calc
        self.new_Cal = self.meal_calc
        self.remain_Cal = round(self.calc - self.new_Cal,2)
        super(Meal, self).save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('calorie:result')
