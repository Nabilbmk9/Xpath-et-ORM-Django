
from django.contrib import admin
from django.urls import path
import myapp.views as views

urlpatterns = [
    path('', views.save_personne, name='save-personne'),
    path('get-personnes', views.get_personnes, name='get-personnes'),
    path('admin/', admin.site.urls),
]
