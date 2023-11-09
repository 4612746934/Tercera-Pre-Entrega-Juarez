from django.urls import path
from . import views 
from mi_blog.views import (eliminar_familiar,eliminar_amigo, eliminar_viaje)

app_name = 'mi_blog'

urlpatterns = [
    path('familiares/', views.lista_familiares, name='lista_familiares'),
    path('amigos/', views.lista_amigos, name='lista_amigos'),
    path('viajes/', views.lista_viajes, name='lista_viajes'),
    path('familiares/crear/', views.crear_familiar, name='crear_familiar'),
    path('amigos/crear/', views.crear_amigo, name='crear_amigo'),
    path('viajes/crear/', views.crear_viaje, name='crear_viaje'),
    path('buscar/', views.buscar, name='buscar'),
    path("eliminar_familiar/<int:id>/", eliminar_familiar, name="eliminar_familiar"),
    path("eliminar_amigo/<int:id>/", eliminar_amigo, name="eliminar_amigo"),
    path("eliminar_viaje/<int:id>/", eliminar_viaje, name="eliminar_viaje"),
]
