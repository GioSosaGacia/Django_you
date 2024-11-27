from django.http import HttpResponse, JsonResponse

# la función render se utiliza para renderizar (generar) una respuesta HTTP que incluye contenido HTML a partir de una plantilla (template)
from django.shortcuts import render, redirect

from .models import Project,Task

#En vez de que nos muestre un erro, haremos que cuando no encuentre un dato mande el error 404 not found importando, la cual permite obtener un objeto y si no existe envia 404
from django.shortcuts import get_object_or_404
#importamos forms
from .forms import CreateNewTask

#Create your views here. lo que puede ver el cliente en pantalla
#orm interactua con la base de datos el cual ya tiene consultas predefinidas
def index(request):
    title = '¡Django Course!'
    #sin render -> return HttpResponse('Index Page')
    #con render
    return render(request,'index.html',{
        'title' : title
    })

#se aplica params mediante el uso de una variable 
def hello(request,id):
    #%s = indica que recibora un parametro o variable, %id es la variable que recibira
    return HttpResponse('<h1>Hello world %s</h1>' %id)

def about(request):
    username = 'Giovanni Sosa'
    #return HttpResponse('<h2>About</h2>')
    return render(request,'about.html',{
        'username' : username
    })


#Params y Modelos
def projects(request):
    #Hacemos el qwery set = conjunto de elementos e importamos JsonResponse 
    #projects = list(Project.objects.values())
    
    #creamos la consulta
    projects = Project.objects.all()
    
#El parámetro safe=False se utiliza al devolver datos en formato JSON desde una vista de Django
#safe=False en JsonResponse El parámetro safe=False se utiliza para decirle a Django que puede convertir cualquier objeto Python (no solo diccionarios) a JSON.
    #return JsonResponse(projects, safe=False)
    
    return render(request,'projects/project.html', {
        'projects':projects
    })


# quitamos el parametro de id para ver el ejemplo con render y uso de templates
def tasks(request):
    #task =Task.objects.get(id=id)
    #La linea superior la cambiamos por, practicamente es lo mismo pero con diferente funcion 
    #task = get_object_or_404(Task, id=id)
    #return HttpResponse('task: %s' %task.title)
    
    #Ciclo for
    tasks = Task.objects.all()
    return render(request,'task/tasks.html', {
        'tasks':tasks
    })
    
    
def create_task(request):    
    if request.method == 'GET':
        #SHOW INTERFACE, si ce usa el metodo GET vamos a renderizar 
        return render(request, 'task/create_task.html', {
            'form': CreateNewTask()
        })
        #caso contrario -> POST: guardamos los datos
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'],project_id=2)
        #done no lo ocupamos agregar ya que es booleano y por defecto es false
        #redirect redirecciona los datos agregado a un url en especifico 
        return redirect('/tasks/')  
    
