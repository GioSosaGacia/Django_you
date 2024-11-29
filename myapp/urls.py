

from django.urls import path
from . import views


#creamos un archivo urls.py para seccionar las urls por aplicación 
urlpatterns = [
    #De esta manera podemos recibir parametros en la misma ruta agregar pico parentesis<con el tipo de dato y nombre de la variable>
    path('hello/<int:id>', views.hello, name='hello'),
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    #path('tasks/<int:id>', views.tasks),
    #con render
    path('tasks/', views.tasks, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_project/', views.create_project, name='create_project'),
]
