from django.conf.urls import url, include
from django.contrib import admin
from home.views import home_view,contact_view
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    url(r'^$', home_view, name='home'),

    url(r'^contact/', contact_view, name='contact'),
    url(r'^accounts/', include('accounts.urls')),

    url(r'^calorie/', include('calorie.urls')),

    url(r'^admin/', admin.site.urls),
]
urlpatterns += staticfiles_urlpatterns()

