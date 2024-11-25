

from django.urls import path
from . import views


#creamos un archivo urls.py para seccionar las urls por aplicación 
urlpatterns = [
    #De esta manera podemos recibir parametros en la misma ruta agregar pico parentesis<con el tipo de dato y nombre de la variable>
    path('hello/<int:id>', views.hello),
    path('about/', views.about),
    path('index/', views.index),
    path('projects/', views.projects),
    #path('tasks/<int:id>', views.tasks),
    #con render
    path('tasks/', views.tasks)
]
