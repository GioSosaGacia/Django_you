from django.contrib import admin
from .models import Project, Task

# Register your models here, para visualizarlo en el servidor con la interfaz grafica, solo dbemos importar los modelos y estos se podran vizualizar desde la interfaz
admin.site.register(Project)
admin.site.register(Task)
