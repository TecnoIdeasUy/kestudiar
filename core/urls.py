from django.urls import path
from .views import Inicio, loginInstitucion, login, instituciones, institucion, registroInst, estudiantes, estudiante
from .views import registroEst, eliminar_curso, locacion, eliminar_locacion, curso, cursoM, locacionM, eliminar_requisito
from .views import requisitoC, requisito, eliminar_materia, materiaC, materia, verCurso

urlpatterns = [
    path('', Inicio.as_view(), name = 'home'),
    path('loginInstitucion/<mensaje>', loginInstitucion, name = 'loginInstitucion'),
    path('login/<mensaje>', login, name = 'login'),
    path('instituciones/<id>/', instituciones, name = 'instituciones'),
    path('institucion/<id>/', institucion, name = 'institucion'),
    path('curso/<id>/<nombre>', curso, name = 'curso'),
    path('cursoM/<id>/<institucion>/<nombre>/', cursoM, name = 'cursoM'),
    path('locacion/<id>/<nombre>', locacion, name = 'locacion'),
    path('locacionM/<id>/<institucion>/<nombre>', locacionM, name = 'locacionM'),
    path('requisitoC/<id>/<institucion>/<nombre>/<cNombre>', requisitoC, name = 'requisitoC'),
    path('requisito/<id>/<institucion>/<nombre>/<cNombre>', requisito, name = 'requisito'),
    path('materiaC/<id>/<institucion>/<nombre>/<cNombre>', materiaC, name = 'materiaC'),
    path('materia/<id>/<institucion>/<nombre>/<cNombre>', materia, name = 'materia'),
    path('registroInst/', registroInst, name = 'registroInst'),
    path('estudiantes/<id>', estudiantes, name = 'estudiantes'),
    path('verCurso/<id>/<nombre>/', verCurso, name = 'verCurso'),
    path('estudiante/<id>/', estudiante, name = 'estudiante'),
    path('registroEst/', registroEst, name = 'registroEst'),
    path('eliminar_curso/<id>/<institucion>', eliminar_curso, name = 'eliminar_curso'),
    path('eliminar_locacion/<id>/<institucion>', eliminar_locacion, name = 'eliminar_locacion'),
    path('eliminar_requisito/<id>/<curso>/<institucion>/<nombre>', eliminar_requisito, name = 'eliminar_requisito'),
    path('eliminar_materia/<id>/<curso>/<institucion>/<nombre>', eliminar_materia, name = 'eliminar_materia')
]
