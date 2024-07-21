from django.contrib import admin
from django.urls import path, include
from AppColegio.views import *

from .views import editProfile

from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('about/', about, name="about"),
       
    
    
    path('listaCursos/', CursoList.as_view(), name="ListaCursos"),
    path('detalleCurso/<pk>/', CursoDetail.as_view(), name="DetalleCurso"),
    path('editarCurso/<pk>/', CursoUpdate.as_view(), name="EditarCurso"),
    path('crearCurso/', CursoCreate.as_view(), name="CrearCurso"),
    path('eliminarCurso/<pk>/', CursoDelete.as_view(), name="EliminarCurso"),
    
    # path('entregableformulario/', entregableFormulario, name="EntregableFormulario"),
    path('listaEntregables/', EntregableList.as_view(), name="ListaEntregables"),
    path('detalleEntregable/<pk>/', EntregableDetail.as_view(), name="DetalleEntregable"),
    path('editarEntregable/<pk>/', EntregableUpdate.as_view(), name="EditarEntregable"),
    path('crearEntregable/', EntregableCreate.as_view(), name="CrearEntregable"),
    path('eliminarEntregable/<pk>/', EntregableDelete.as_view(), name="EliminarEntregable"),
    
    
    path('listaProfesores/', ProfesorList.as_view(), name="ListaProfesores"),
    path('detalleProfesor/<pk>/', ProfesorDetail.as_view(), name="DetalleProfesor"),
    path('editarProfesor/<pk>/', ProfesorUpdate.as_view(), name="EditarProfesor"),
    path('crearProfesor/', ProfesorCreate.as_view(), name="CrearProfesor"),
    path('eliminarProfesor/<pk>/', ProfesorDelete.as_view(), name="EliminarProfesor"),
   
    # path('estudianteformulario/', estudianteFormulario, name="EstudianteFormulario"),
    path('listaEstudiantes/', EstudianteList.as_view(), name="ListaEstudiantes"),
    path('detalleEstudiante/<pk>/', EstudianteDetail.as_view(), name="DetalleEstudiante"),
    path('editarEstudiante/<pk>/', EstudianteUpdate.as_view(), name="EditarEstudiante"),
    path('crearEstudiante/', EstudianteCreate.as_view(), name="CrearEstudiante"),
    path('eliminarEstudiante/<pk>/', EstudianteDelete.as_view(), name="EliminarEstudiante"),


      
    #___ Busquedas
    path('buscarCursos/', buscarCursos, name="buscarCursos"),
    path('encontrarCursos/', encontrarCursos, name="encontrarCursos"),


    #___ Login / Logout / Registration      
    path('registro/', register, name="registro"),    
    path('login/', user_login, name="Login"),
    path('logout/', user_logout, name="Logout"),


    #___ Edición de Perfil y Avatar      
    path('editarPerfil/', editProfile, name="editarPerfil" ),
    path('<int:pk>/password/', CambiarClave.as_view(), name="cambiarClave"),
    path('agregarAvatar/', agregarAvatar, name="agregar_avatar" ),            

]