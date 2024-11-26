from django.db import models

# Create your models here.

#descargamos sqlbrowser para poder visualizar la base de datos de sqlite
#en este apartado creamos los modelas de la base de datos, con sus variable y tipos de datos.

# Al aplicar makemigration myapp hace las migraciones unucamente de nuestra aplicacion myapp y nos crea el archivo 0001_initial.py que es la referencia de la tabla creada
# myapp\migrations\0001_initial.py
    #- Create model Project
class Project(models.Model):
    name = models.CharField(max_length=200)
    
#Con este metodo nos mostrará el nombre de los objetos creados en Project, ya que abteriormente solo mostraba object:1,2,3 etc
    def __str__(self):
        return self.name
    
    #Para crear tareas debemos de especificar a que aplicación pertenece, en este caso vamos a relacionar Project con Task, con el uso de FK, usando en on_delete=models.cascade si eliminasmos de latabla Project tambien se eliminara en Task
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    #con la eliminacion en cascada si deseamos eliminar un proyecto lo eliminara y si el mismo esta relacionado a + proyectos o raeas eliminara todo lo relacionado a tal projecto
    project = models.ForeignKey(Project, on_delete=models.CASCADE) 
    #podemos agregar mas campos a la table solo de debe de hacer el makemigrations y migrate
    done = models.BooleanField(default=False)
    
    def __str__(self):
         return self.title + '-' + self.project.name


