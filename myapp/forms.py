from django import forms

# Crear formularios para enviaros al html, no confundir con la base de datos se crea de manera similar pero unicamente es para la creacion del mismo formulario


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(
        label="Descripcion de la tarea", widget=forms.Textarea)


class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto", max_length=200)
