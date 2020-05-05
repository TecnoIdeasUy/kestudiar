from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length = 30, blank = False, null = False)

    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Paises'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    pais = models.ForeignKey(Pais, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 30, blank = False, null = False)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'
        ordering = ['pais', 'nombre']

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    pais = models.ForeignKey(Pais, on_delete = models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 30, blank = False, null = False)

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Barrio(models.Model):
    pais = models.ForeignKey(Pais, on_delete = models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 30, blank = False, null = False)

    class Meta:
        verbose_name = 'Barrio'
        verbose_name_plural = 'Barrios'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class TipoInstitucion(models.Model):
    nombre = models.CharField(max_length = 30, blank = False, null = False)

    class Meta:
        verbose_name = 'Tipo de Institución'
        verbose_name_plural = 'Tipos de Instituciones'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Institucion(models.Model):
    nombre = models.CharField(max_length = 100, blank = False, null = False)
    tipoInstitucion = models.ForeignKey(TipoInstitucion, on_delete = models.CASCADE)
    direccion = models.CharField(max_length = 100, blank = False, null = False)
    pais = models.ForeignKey(Pais, on_delete = models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE)
    barrio = models.ForeignKey(Barrio, on_delete = models.CASCADE)
    telefono = models.CharField(max_length = 100, blank = True, null = True)
    eMail = models.CharField(max_length = 100, blank = True, null = True)
    web = models.CharField(max_length = 100, blank = True, null = True)
    usuario = models.CharField(max_length = 30, unique=True, blank = False, null = False)
    password = models.CharField(max_length = 30, blank = False, null = False)

    class Meta:
        verbose_name = 'Institución'
        verbose_name_plural = 'Instituciones'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Locacion(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 100, blank = False, null = False)
    direccion = models.CharField(max_length = 100, blank = False, null = False)
    pais = models.ForeignKey(Pais, on_delete = models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE)
    barrio = models.ForeignKey(Barrio, on_delete = models.CASCADE)
    telefono = models.CharField(max_length = 100, blank = True, null = True)
    eMail = models.CharField(max_length = 100, blank = True, null = True)

    class Meta:
        verbose_name = 'Locación'
        verbose_name_plural = 'Locaciones'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    institucion = models.ForeignKey(Institucion, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 100, blank = False, null = False)
    duración = models.CharField(max_length = 20, blank = False, null = False)
    titulo = models.CharField(max_length = 100, blank = False, null = False)
    locacion = models.ForeignKey(Locacion, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class CursoAux(models.Model):
    idCurso = models.IntegerField(blank = True, null = True)
    nombre = models.CharField(max_length = 100, blank = False, null = False)
    duración = models.CharField(max_length = 20, blank = False, null = False)
    titulo = models.CharField(max_length = 100, blank = False, null = False)
    institucion = models.CharField(max_length = 100, blank = True, null = True)

    class Meta:
        verbose_name = 'CursoAux'
        verbose_name_plural = 'CursosAux'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class NivelEstudio(models.Model):
    nombre = models.CharField(max_length = 30, blank = False, null = False)

    class Meta:
        verbose_name = 'Nivel de estudio'
        verbose_name_plural = 'Nivel de estudios'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length = 100, blank = False, null = False)
    pais = models.ForeignKey(Pais, on_delete = models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE)
    telefono = models.CharField(max_length = 100, blank = True, null = True)
    eMail = models.CharField(max_length = 100, blank = True, null = True)
    nivelEstudio = models.ForeignKey(NivelEstudio, on_delete = models.CASCADE)
    usuario = models.CharField(max_length = 30, unique=True, blank = False, null = False)
    password = models.CharField(max_length = 30, blank = False, null = False)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Requisito(models.Model):
    nombre = models.CharField(max_length = 100, blank = False, null = False)

    class Meta:
        verbose_name = 'Requisito'
        verbose_name_plural = 'Requisitos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class RequisitosCurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    requisito = models.ForeignKey(Requisito, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Requisito curso'
        verbose_name_plural = 'Requisitos curso'
        ordering = ['requisito']

    def __str__(self):
        return self.requisito.nombre

class Materia(models.Model):
    nombre = models.CharField(max_length = 100, blank = False, null = False)

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class MateriasCurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete = models.CASCADE)
    semestre = models.IntegerField(default = 1, blank = False, null = False)
    horas = models.IntegerField(default = 0, blank = False, null = False)
    creditos = models.IntegerField(default = 0, blank = True, null = True)
    descripcion = models.TextField(blank = True, null = True)

    class Meta:
        verbose_name = 'Materia curso'
        verbose_name_plural = 'Materias curso'
        ordering = ['curso']

    def __str__(self):
        return self.curso.nombre
