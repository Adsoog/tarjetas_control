from django.urls import include, path
from .views import crear_proceso, mi_vista_compleja, lista_procesos, lista_subprocesos, lista_tareas # Asegúrate de importar la vista correctamente
from . import views

urlpatterns = [
    path('procesos/', mi_vista_compleja, name='procesos_sin_id'),
    path('procesos/<int:proceso_id>/<int:subproceso_id>/', mi_vista_compleja, name='procesos_con_id'),
    path('procesos/<int:proceso_id>/', mi_vista_compleja, name='procesos_con_id'),

    #lista procesos
    path('lista_procesos/', lista_procesos, name='lista_procesos'),
    #lista de subprocesos
    path('lista_subprocesos/', lista_subprocesos, name='lista_subprocesos'),
    #lista de tareas
    path('lista_tareas/', lista_tareas, name='lista_tareas'),



    # urls para la ceracion de proesos subproceso y tareas
    path('crear-proceso/', crear_proceso, name='crear_proceso'),
    path('proceso/<int:proceso_id>/', views.ver_proceso, name='ver_proceso'),


    path('subproceso/<int:subproceso_id>/', views.ver_subproceso, name='ver_subproceso'),
]
