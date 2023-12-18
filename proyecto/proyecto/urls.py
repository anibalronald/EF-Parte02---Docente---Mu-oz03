
from django.contrib import admin
from django.urls import path
from miapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('crearcurso/',views.crearcurso,name='crearcurso'),
    path('creardocente/',views.creardocente,name='creardocente'),
    path('inicio/',views.inicio,name='inicio'),
    path('integrantes/',views.integrantes,name='integrantes'),
    path('listarcurso/',views.listarcurso,name='listarcurso'),
    path('listardocente/',views.listardocente,name='listardocente'),
]