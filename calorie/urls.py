from django.conf.urls import url
from .views import *

app_name = "calorie"

urlpatterns = [

    url(r'^calorie/$', calorie_create, name="create"),

    url(r'^detail/$', calorie_detail, name="detail"),

    url(r'^meal/$', mealcalorie, name="meal"),

    url(r'^result/$', result_detail, name="result"),

]
