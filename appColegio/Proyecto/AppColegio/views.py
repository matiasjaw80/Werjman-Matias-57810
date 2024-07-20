from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import *
from .models import *

# Create your views here.
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from .forms import RegistroUsuariosForm, UserEditForm, AvatarFormulario

from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#______________________________________________________________________________________

@login_required
def inicio(self):
    lista_cursos = Curso.objects.all()
    return render(self, "inicio.html", {"cursos": lista_cursos})

@login_required
def profesores(self):
    lista_profesores = Profesor.objects.all()
    return render(self, "profesores.html", {"profesores": lista_profesores})

@login_required
def estudiante(self):
    lista_estudiantes = Estudiante.objects.all()
    return render(self, "estudiantes.html", {"estudiantes": lista_estudiantes})

@login_required
def entregables(self):
    lista_entregables = Entregable.objects.all()

    return render(self, "entregables.html", {"entregables": lista_entregables})

@login_required
def cursos(self):
    lista_cursos = Curso.objects.all()
    return render(self, "cursos.html", {"cursos": lista_cursos})


#___Formularios

def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            curso = Curso(
                nombre=data['nombre'], comision=data['comision'], codigo=data['codigo'], imagen=data['imagen'], estudiante=data['estudiante'])
            curso.save()
            lista_cursos = Curso.objects.all()
            return render(request, 'cursos.html', {"cursos": lista_cursos})
        else:
            miFormulario = CursoFormulario()
            return render(request, "cursoFormulario.html", {"miFormulario": miFormulario, "error": "Datos de formulario invalidos"})
    else:
        miFormulario = CursoFormulario()
        return render(request, "cursoFormulario.html", {"miFormulario": miFormulario})

@login_required
def editarCurso(request, id):
    Curso = Curso.objects.get(id=id)
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            Curso.nombre = data['nombre']
            Curso.comision = data['comision']
            Curso.codigo = data['codigo']
            Curso.imagen = data['imagen']
            Curso.save()
            lista_cursos = Curso.objects.all()
            return render(request, 'Curso.html', {"Curso": lista_cursos})
        else:
            miFormulario = CursoFormulario()
            return render(request, "cursoFormulario.html", {"miFormulario": miFormulario, "error": "Datos de formulario invalidos"})
    else:
        miFormulario = ProfesorFormulario(initial={
            "nombre": Curso.nombre,
            "comision": Curso.comision,
            "codigo": Curso.codigo,
            "imagen": Curso.imagen,
        })
        return render(request, "editarCurso.html", {"miFormulario": miFormulario, "id": cursos.id})

@login_required
def estudianteFormulario(request):
    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            print(data)
            estudiante = Estudiante(
                nombre=data['nombre'], apellido=data['apellido'], email=data['email'])
            estudiante.save()
            lista_estudiantes = Estudiante.objects.all()
            return render(request, 'estudiantes.html', {"estudiantes": lista_estudiantes})
        else:
            miFormulario = EstudianteFormulario()
            return render(request, "estudianteFormulario.html", {"miFormulario": miFormulario, "error": "Datos de formulario invalidos"})
    else:
        miFormulario = EstudianteFormulario()
        return render(request, "estudianteFormulario.html", {"miFormulario": miFormulario})

@login_required
def eliminarEstudiante(request, id):
    if request.method == 'POST':
        estudiante = Estudiante.objects.get(id=id)
        estudiante.delete()
        lista_estudiantes = estudiante.objects.all()
        return render(request, 'estudiantes.html', {"estudiantes": lista_estudiantes})

@login_required
def editarEstudiante(request, id):
    estudiante = Estudiante.objects.get(id=id)
    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            estudiante.nombre = data['nombre']
            estudiante.apellido = data['apellido']
            estudiante.email = data['email']
            estudiante.save()
            lista_estudiantes = Estudiante.objects.all()
            return render(request, 'estudiantes.html', {"estudiantes": lista_estudiantes})
        else:
            miFormulario = EstudianteFormulario()
            return render(request, "estudianteFormulario.html", {"miFormulario": miFormulario, "error": "Datos de formulario invalidos"})
    else:
        miFormulario = ProfesorFormulario(initial={
            "nombre": estudiante.nombre,
            "apellido": estudiante.apellido,
            "email": estudiante.email,
        })
        return render(request, "editarEstudiante.html", {"miFormulario": miFormulario, "id": estudiante.id})

@login_required
def profesorFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            profesor = Profesor(
                nombre=data['nombre'], apellido=data['apellido'], email=data['email'], profesion=data['profesion'])
            profesor.save()
            lista_profesores = Profesor.objects.all()
            return render(request, 'profesores.html', {"profesores": lista_profesores})
        else:
            miFormulario = ProfesorFormulario()
            return render(request, "profesorFormulario.html", {"miFormulario": miFormulario, "error": "Datos de formulario invalidos"})
    else:
        miFormulario = ProfesorFormulario()
        return render(request, "profesorFormulario.html", {"miFormulario": miFormulario})

@login_required
def eliminarProfesor(request, id):
    if request.method == 'POST':
        profesor = Profesor.objects.get(id=id)
        profesor.delete()
        lista_profesores = Profesor.objects.all()
        return render(request, 'profesores.html', {"profesores": lista_profesores})

@login_required
def editarProfesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            profesor.nombre = data['nombre']
            profesor.email = data['email']
            profesor.apellido = data['apellido']
            profesor.profesion = data['profesion']
            profesor.save()
            lista_profesores = Profesor.objects.all()
            return render(request, 'profesores.html', {"profesores": lista_profesores})
        else:
            miFormulario = ProfesorFormulario()
            return render(request, "profesorFormulario.html", {"miFormulario": miFormulario, "error": "Datos de formulario invalidos"})
    else:
        miFormulario = ProfesorFormulario(initial={
            "nombre": profesor.nombre,
            "email": profesor.email,
            "apellido": profesor.apellido,
            "profesion": profesor.profesion,
        })
        return render(request, "editarProfesor.html", {"miFormulario": miFormulario, "id": profesor.id})

@login_required
def entregableFormulario(request):
    if request.method == 'POST':
        miFormulario = EntregableFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            entregable = Entregable(
                nombre=data['nombre'], fecha_entrega=data['fecha_entrega'], entregado=data['entregado'])
            entregable.save()
            lista_entregables = Entregable.objects.all()
            return render(request, 'entregables.html', {"entregables": lista_entregables})
        else:
            miFormulario = EntregableFormulario()
            return render(request, "entregableFormulario.html", {"miFormulario": miFormulario, "error": "Datos de formulario invalidos"})
    else:
        miFormulario = EntregableFormulario()
        return render(request, "entregableFormulario.html", {"miFormulario": miFormulario})

@login_required
def editarEntregable(request, id):
    Entregable = Entregable.objects.get(id=id)
    if request.method == 'POST':
        miFormulario = EntregableFormulario(request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            Entregable.nombre = data['nombre']
            Entregable.fecha = data['fecha']
            Entregable.entregado = data['entregado']
            Entregable.save()
            lista_Entregable = Entregable.objects.all()
            return render(request, 'Entregable.html', {"Entregable": lista_Entregable})
        else:
            miFormulario = EntregableFormulario()
            return render(request, "EntregableFormulario.html", {"miFormulario": miFormulario, "error": "Datos de formulario invalidos"})
    else:
        miFormulario = EntregableFormulario(initial={
            "nombre": Entregable.nombre,
            "fecha": Entregable.fecha,
            "entregado": Entregable.entregado,
        })
        return render(request, "editarCurso.html", {"miFormulario": miFormulario, "id": cursos.id})

@login_required
def eliminarEntregable(request, id):
    if request.method == 'POST':
        profesor = Profesor.objects.get(id=id)
        profesor.delete()
        lista_profesores = Profesor.objects.all()
        return render(request, 'profesores.html', {"profesores": lista_profesores})



#______________________________________________________________________________________



#___Busqueda

@login_required
def buscarCursos(request):
    return render(request, 'buscar.html')

def encontrarCursos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        cursos = Curso.objects.filter(nombre__icontains=patron)
        contexto = {'cursos': cursos}    
    else:
        contexto = {'cursos': Curso.objects.all()}
        
    return render(request, "buscar.html", contexto)


#____Class______

def index(request):
    return render(request, 'index.html')



#____CURSO______

class CursoList(LoginRequiredMixin, ListView):
    model = Curso
    template_name = 'listaCursos.html'
    context_object_name = 'cursos'


class CursoDetail(DetailView):
    model = Curso
    template_name = 'detalleCurso.html'
    context_object_name = 'curso'


class CursoUpdate(UpdateView):
    model = Curso
    template_name = 'editarCurso.html'
    fields = ['nombre', 'comision', 'codigo', 'imagen']
    success_url = '/app-colegio/listaCursos/'


class CursoDelete(DeleteView):
    model = Curso
    template_name = 'eliminarCurso.html'
    success_url = '/app-colegio/listaCursos/'
    context_object_name = 'curso'


class CursoCreate(CreateView):
    model = Curso
    template_name = 'crearCurso.html'
    fields = ['nombre', 'comision', 'codigo', 'imagen']
    success_url = '/app-colegio/listaEntregables/'

#____ENTREGABLE______

class EntregableList(ListView):
    model = Entregable
    template_name = 'listaEntregables.html'
    context_object_name = 'entregables'

class EntregableDetail(DetailView):
    model = Entregable
    template_name = 'detalleEntregable.html'
    context_object_name = 'entregable'

class EntregableUpdate(UpdateView):
    model = Entregable
    template_name = 'editarEntregable.html'
    fields = ['nombre', 'fecha_entrega', 'entregado']
    success_url = '/app-colegio/listaEntregables/'

class EntregableDelete(DeleteView):
    model = Entregable
    template_name = 'eliminarEntregable.html'
    success_url = '/app-colegio/listaEntregables/'
    context_object_name = 'entregable'

class EntregableCreate(CreateView):
    model = Entregable
    template_name = 'crearEntregable.html'
    fields = ['nombre', 'fecha_entrega', 'entregado']
    success_url = '/app-colegio/listaEntregables/'

#____PROFESORES______

class ProfesorList(ListView):
    model = Profesor
    template_name = 'listaProfesores.html'
    context_object_name = 'Profesor'

class ProfesorDetail(DetailView):
    model = Profesor
    template_name = 'detalleProfesor.html'
    context_object_name = 'Profesor'

class ProfesorUpdate(UpdateView):
    model = Profesor
    template_name = 'editarProfesor.html'
    fields = ['nombre', 'apellido', 'email', 'profesion', 'cursos']
    success_url = '/app-colegio/listaProfesores/'

class ProfesorDelete(DeleteView):
    model = Profesor
    template_name = 'eliminarProfesor.html'
    success_url = '/app-colegio/listaProfesores/'
    context_object_name = 'profesor'

class ProfesorCreate(CreateView):
    model = Profesor
    template_name = 'crearProfesor.html'
    fields = ['nombre', 'apellido', 'email', 'profesion', 'cursos']
    success_url = '/app-colegio/listaProfesores/'


#_______ESTUDIANTES_______

class EstudianteList(ListView):
    model = Estudiante
    template_name = 'listaEstudiantes.html'
    context_object_name = 'Estudiante'

class EstudianteDetail(DetailView):
    model = Estudiante
    template_name = 'detalleEstudiante.html'
    context_object_name = 'Estudiante'

class EstudianteUpdate(UpdateView):
    model = Estudiante
    template_name = 'editarEstudiante.html'
    fields = ['nombre', 'apellido', 'email', 'cursos']
    success_url = '/app-colegio/listaEstudiantes/'

class EstudianteDelete(DeleteView):
    model = Estudiante
    template_name = 'eliminarEstudiante.html'
    success_url = '/app-colegio/listaEstudiantes/'
    context_object_name = 'Estudiante'

class EstudianteCreate(CreateView):
    model = Estudiante
    template_name = 'crearEstudiante.html'
    fields = ['nombre', 'apellido', 'email', 'cursos']
    success_url = '/app-colegio/listaEstudiantes/'



#______________________________________________________________________________________
#___Login

def user_login(request):
    if request.method == 'POST':
        miFormulario = AuthenticationForm(request, data=request.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data['username']
            password = data['password']
            user = authenticate(username=usuario, password=password)
            if user:
                login(request, user)
                
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar
                                
                return render(request, "inicio.html")
            else:
                miFormulario = AuthenticationForm()
                return render(request, 'userLogin.html', {'miFormulario': miFormulario, 'error': 'credenciales de usuario incorrectas'})
        else:
            miFormulario = AuthenticationForm()
            return render(request, 'userLogin.html', {'miFormulario': miFormulario, 'error': 'Ha ocurrido un error, por favor intentalo de nuevo'})
    else:
        miFormulario = AuthenticationForm()
        return render(request, 'userLogin.html', {'miFormulario': miFormulario})

def user_logout(request):
    logout(request)
    return render(request, "userLogout.html")


def about(request):
    return render(request, "about.html")


#______________________________________________________________________________________


def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            miForm.save()
            return redirect(reverse_lazy('Inicio'))
    else:
        miForm = RegistroUsuariosForm()

    return render(request, "registro.html", {"form": miForm})  

#______________________________________________________________________________________

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miform = UserEditForm(request.POST)
        if miform.is_valid():
            user = User.objects.get(username=usuario)
            usuario.email = miform.cleaned_data.get('email')
            usuario.first_name = miform.cleaned_data.get('first_name')
            usuario.last_name = miform.cleaned_data.get('last_name')
            usuario.save()
            return redirect(reverse_lazy,('Inicio'))
    else:
        miform = UserEditForm(instance=usuario)
    return render(request, "editarPerfil.html", {"form": miform})

#______________________________________________________________________________________


class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "cambiarClave.html"
    success_url = reverse_lazy("inicio")


#______________________________________________________________________________________    
    
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) # Diferente a los forms tradicionales
        if form.is_valid():
            u = User.objects.get(username=request.user)

            # ____ Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            # ____ Guardar el nuevo
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___ Hago que la url de la imagen viaje en el request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"inicio.html")
    else:
        form = AvatarFormulario()
    return render(request, "agregarAvatar.html", {'form': form })