from django.contrib import admin
from .models import Pais
from .models import Departamento
from .models import Ciudad
from .models import Barrio
from .models import TipoInstitucion
from .models import Institucion
from .models import Curso
from .models import NivelEstudio
from .models import Estudiante
from .models import Locacion
from .models import Requisito
from .models import RequisitosCurso
from .models import Materia
from .models import MateriasCurso

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('pais', 'nombre')
    search_fields = ['nombre']
    list_filter = ('pais',)

class CiudadAdmin(admin.ModelAdmin):
    list_display = ('pais', 'departamento', 'nombre')
    search_fields = ['nombre']
    list_filter = ('pais', 'departamento',)


class BarrioAdmin(admin.ModelAdmin):
    list_display = ('pais', 'departamento', 'ciudad', 'nombre')
    search_fields = ['nombre']
    list_filter = ('pais', 'departamento', 'ciudad', )

class InstitucionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipoInstitucion', 'pais', 'departamento', 'ciudad', 'web')
    search_fields = ['nombre']
    list_filter = ('tipoInstitucion', 'pais', 'departamento', 'ciudad', )

class CursoAdmin(admin.ModelAdmin):
    list_display = ('institucion', 'nombre', 'duración', 'titulo')
    search_fields = ['nombre']
    list_filter = ('institucion', )


class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'departamento', 'ciudad', 'nivelEstudio')
    search_fields = ['nombre']
    list_filter = ('nivelEstudio', 'pais', 'departamento', 'ciudad', )

class LocacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'departamento', 'ciudad', )
    search_fields = ['nombre']
    list_filter = ('pais', 'departamento', 'ciudad', )

admin.site.register(Pais)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Barrio, BarrioAdmin)
admin.site.register(TipoInstitucion)
admin.site.register(Institucion, InstitucionAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(NivelEstudio)
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Locacion, LocacionAdmin)
admin.site.register(Requisito)
admin.site.register(RequisitosCurso)
admin.site.register(Materia)
admin.site.register(MateriasCurso)
