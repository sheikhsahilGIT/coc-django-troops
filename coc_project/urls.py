from django.contrib import admin
from django.urls import path
from troops.views import home   # change to coc_troops.views.home if app name changed

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),   # root URL shows our troop page
]