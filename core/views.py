from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Curso, NivelEstudio, Pais, Departamento, Ciudad, Barrio, TipoInstitucion, Institucion, Estudiante, Locacion
from .models import Requisito, RequisitosCurso, Materia, MateriasCurso, Materia, CursoAux

class Inicio(TemplateView):
    template_name = 'core/home.html'

def loginInstitucion(request, mensaje):
    if request.POST:
        #Buscamos el usuario para logearse
        try:
            instituto = Institucion.objects.get(usuario =  request.POST.get('txtUsuario'))
            if instituto.password == request.POST.get('txtContraseña'):
                return redirect('instituciones', instituto.id)
            else:
                mensaje = 'Contraseña incorrecta'
                return redirect('loginInstitucion',  {'mensaje':mensaje})
        except:
            mensaje = 'Usuario inexistente'
            return redirect('loginInstitucion',  {'mensaje':mensaje})

    return render(request, 'core/loginInstitucion.html', {'mensaje':mensaje})

def login(request, mensaje):
    if request.POST:
        #Buscamos el usuario para logearse
        try:
            estudiante = Estudiante.objects.get(usuario =  request.POST.get('txtUsuario'))
            if estudiante.password == request.POST.get('txtContraseña'):
                return redirect('estudiantes', estudiante.id)
            else:
                mensaje = 'Contraseña incorrecta'
                return redirect('login', {'mensaje':mensaje})
        except Exception:
            mensaje = 'Usuario inexistente'
            return redirect('login',  {'mensaje':mensaje})

    return render(request, 'core/login.html', {'mensaje':mensaje})


def instituciones(request, id):
    #Buscamos la institución a cargar
    instituto = Institucion.objects.get(id=id)
    cursos = Curso.objects.filter(institucion=id).order_by('nombre')

    parametros = {
        'instituto':instituto,
        'cursos':cursos
    }

    return render(request, 'core/instituciones.html', parametros)

def institucion(request, id):
    #Buscamos la institución a modificar
    instituto = Institucion.objects.get(id=id)

    tipos = TipoInstitucion.objects.all().order_by('nombre')
    paises = Pais.objects.all().order_by('nombre')
    departamentos = Departamento.objects.all().order_by('nombre')
    ciudades = Ciudad.objects.all().order_by('nombre')
    barrios = Barrio.objects.all().order_by('nombre')
    cursos = Curso.objects.filter(institucion=id).order_by('nombre')
    local = Locacion.objects.filter(institucion=id).order_by('nombre')

    parametros = {
        'instituto': instituto,
        'tipos':tipos,
        'paises':paises,
        'departamentos':departamentos,
        'ciudades':ciudades,
        'barrios':barrios,
        'cursos':cursos,
        'local':local
    }

    if request.POST:
        instituto = Institucion()
        instituto.id = request.POST.get('txtId')
        instituto.nombre = request.POST.get('txtNombre')
        tipo = TipoInstitucion()
        tipo.id = request.POST.get('cboTipo')
        instituto.tipoInstitucion = tipo
        instituto.direccion = request.POST.get('txtDireccion')
        pais = Pais()
        pais.id = request.POST.get('cboPais')
        instituto.pais = pais
        departamento = Departamento()
        departamento.id = request.POST.get('cboDepartamento')
        instituto.departamento = departamento
        ciudad = Ciudad()
        ciudad.id = request.POST.get('cboCiudad')
        instituto.ciudad = ciudad
        barrio = Barrio()
        barrio.id = request.POST.get('cboBarrio')
        instituto.barrio = barrio
        instituto.telefono = request.POST.get('txtTelefono')
        instituto.eMail = request.POST.get('txtMail')
        instituto.web = request.POST.get('txtWeb')
        instituto.usuario = request.POST.get('txtUsuario')
        instituto.password = request.POST.get('txtPassword')

        try:
            instituto.save()
            messages.success(request, 'Institucion modificada correctamente')
            return redirect("instituciones", id)
        except:
            messages.error(request, 'No se pudo guardar la modificación')

    return render(request, 'core/institucion.html', parametros)

def registroInst(request):
    tipos = TipoInstitucion.objects.all().order_by('nombre')
    paises = Pais.objects.all().order_by('nombre')
    departamentos = Departamento.objects.all().order_by('nombre')
    ciudades = Ciudad.objects.all().order_by('nombre')
    barrios = Barrio.objects.all().order_by('nombre')

    parametros = {
        'tipos':tipos,
        'paises':paises,
        'departamentos':departamentos,
        'ciudades':ciudades,
        'barrios':barrios
    }

    if request.POST:
        instituto = Institucion()
        instituto.nombre = request.POST.get('txtNombre')
        tipo = TipoInstitucion()
        tipo.id = request.POST.get('cboTipo')
        instituto.tipoInstitucion = tipo
        instituto.direccion = request.POST.get('txtDireccion')
        pais = Pais()
        pais.id = request.POST.get('cboPais')
        instituto.pais = pais
        departamento = Departamento()
        departamento.id = request.POST.get('cboDepartamento')
        instituto.departamento = departamento
        ciudad = Ciudad()
        ciudad.id = request.POST.get('cboCiudad')
        instituto.ciudad = ciudad
        barrio = Barrio()
        barrio.id = request.POST.get('cboBarrio')
        instituto.barrio = barrio
        instituto.telefono = request.POST.get('txtTelefono')
        instituto.eMail = request.POST.get('txtMail')
        instituto.web = request.POST.get('txtWeb')
        instituto.usuario = request.POST.get('txtUsuario')
        instituto.password = request.POST.get('txtPassword')

        try:
            instituto.save()
            parametros['mensaje'] = 'Institucion guardada correctamente'
        except:
            parametros['mensaje'] = 'No se pudo guardar la institución'

    return render(request, 'core/registroInst.html', parametros)

def locacion(request, id, nombre):
    tipos = TipoInstitucion.objects.all().order_by('nombre')
    paises = Pais.objects.all().order_by('nombre')
    departamentos = Departamento.objects.all().order_by('nombre')
    ciudades = Ciudad.objects.all().order_by('nombre')
    barrios = Barrio.objects.all().order_by('nombre')
    cursos = Curso.objects.all().order_by('nombre')

    parametros = {
        'tipos':tipos,
        'paises':paises,
        'departamentos':departamentos,
        'ciudades':ciudades,
        'barrios':barrios,
        'cursos':cursos,
        'id':id,
        'nombre':nombre
    }

    if request.POST:
        local = Locacion()
        institucion = Institucion()
        institucion.id = request.POST.get('txtId')
        local.institucion = institucion
        local.nombre = request.POST.get('txtNombre')
        local.direccion = request.POST.get('txtDireccion')
        pais = Pais()
        pais.id = request.POST.get('cboPais')
        local.pais = pais
        departamento = Departamento()
        departamento.id = request.POST.get('cboDepartamento')
        local.departamento = departamento
        ciudad = Ciudad()
        ciudad.id = request.POST.get('cboCiudad')
        local.ciudad = ciudad
        barrio = Barrio()
        barrio.id = request.POST.get('cboBarrio')
        local.barrio = barrio
        local.telefono = request.POST.get('txtTelefono')
        local.eMail = request.POST.get('txtMail')

        try:
            local.save()
            parametros['mensaje'] = 'Locación guardada correctamente'
        except:
            parametros['mensaje'] = 'No se pudo guardar la locación'
        return redirect("institucion", id)

    return render(request, 'core/locacion.html', parametros)

def locacionM(request, id, institucion, nombre):
    #Buscamos la locacion a modificar
    local = Locacion.objects.get(id=id)

    tipos = TipoInstitucion.objects.all().order_by('nombre')
    paises = Pais.objects.all().order_by('nombre')
    departamentos = Departamento.objects.all().order_by('nombre')
    ciudades = Ciudad.objects.all().order_by('nombre')
    barrios = Barrio.objects.all().order_by('nombre')
    cursos = Curso.objects.all().order_by('nombre')

    parametros = {
        'local':local,
        'tipos':tipos,
        'paises':paises,
        'departamentos':departamentos,
        'ciudades':ciudades,
        'barrios':barrios,
        'cursos':cursos,
        'id':id,
        'nombre':nombre,
        'institucion': institucion
    }

    if request.POST:
        local = Locacion()
        local.id = request.POST.get('txtId')
        institucion = Institucion()
        institucion.id = request.POST.get('txtInstitucion')
        local.institucion = institucion
        local.nombre = request.POST.get('txtNombre')
        local.direccion = request.POST.get('txtDireccion')
        pais = Pais()
        pais.id = request.POST.get('cboPais')
        local.pais = pais
        departamento = Departamento()
        departamento.id = request.POST.get('cboDepartamento')
        local.departamento = departamento
        ciudad = Ciudad()
        ciudad.id = request.POST.get('cboCiudad')
        local.ciudad = ciudad
        barrio = Barrio()
        barrio.id = request.POST.get('cboBarrio')
        local.barrio = barrio
        local.telefono = request.POST.get('txtTelefono')
        local.eMail = request.POST.get('txtMail')

        try:
            local.save()
            messages.success(request, 'Locación modificado correctamente')
        except:
            messages.error(request, 'No se pudo guardar la locación')
        return redirect("institucion", request.POST.get('txtInstitucion'))

    return render(request, 'core/locacionM.html', parametros)

def requisitoC(request, id, institucion, nombre, cNombre):
    #Buscamos el curso al que le vamos a agregar un requisito
    requisitosC = RequisitosCurso.objects.filter(curso=id)
    requisito = Requisito.objects.all().order_by('nombre')

    parametros = {
        'requisitosC':requisitosC,
        'requisito':requisito,
        'id':id,
        'institucion':institucion,
        'nombre':nombre,
        'cNombre':cNombre
    }

    if request.POST:
        reqC = RequisitosCurso()
        curso = Curso()
        curso.id = request.POST.get('txtCurso')
        reqC.curso = curso
        req = Requisito()
        req.id = request.POST.get('cboRequisito')
        reqC.requisito = req

        try:
            reqC.save()
            parametros['mensaje'] = 'Requisito guardado correctamente'
        except Exception as inst:
            parametros['mensaje'] = inst

    return render(request, 'core/requisitoC.html', parametros)

def requisito(request, id, institucion, nombre, cNombre):
    requisito = Requisito.objects.all().order_by('nombre')

    parametros = {
        'requisito':requisito,
        'id':id,
        'institucion':institucion,
        'nombre':nombre,
        'cNombre':cNombre
    }

    if request.POST:
        req = Requisito()
        req.nombre = request.POST.get('txtNombre')

        try:
            req.save()
            parametros['mensaje'] = 'Requisito guardado correctamente'
        except Exception as inst:
            parametros['mensaje'] = inst

    return render(request, 'core/requisito.html', parametros)

def materiaC(request, id, institucion, nombre, cNombre):
    #Buscamos el curso al que le vamos a agregar un requisito
    materiasC = MateriasCurso.objects.filter(curso=id)
    materia = Materia.objects.all().order_by('nombre')

    parametros = {
        'materiasC':materiasC,
        'materia':materia,
        'id':id,
        'institucion':institucion,
        'nombre':nombre,
        'cNombre':cNombre
    }

    if request.POST:
        matC = MateriasCurso()
        curso = Curso()
        curso.id = request.POST.get('txtCurso')
        matC.curso = curso
        mat= Materia()
        mat.id = request.POST.get('cboMateria')
        matC.materia = mat
        matC.semestre = request.POST.get('txtSemestre')
        matC.horas = request.POST.get('txtHoras')
        matC.creditos = request.POST.get('txtCreditos')
        matC.descripcion = request.POST.get('txtDescripcion')

        try:
            matC.save()
            parametros['mensaje'] = 'Materia guardada correctamente'
        except Exception as inst:
            parametros['mensaje'] = 'No se pudo guardar la materia'

    return render(request, 'core/materiaC.html', parametros)

def materia(request, id, institucion, nombre, cNombre):
    materia = Materia.objects.all().order_by('nombre')

    parametros = {
        'materia':materia,
        'id':id,
        'institucion':institucion,
        'nombre':nombre,
        'cNombre':cNombre
    }

    if request.POST:
        mat = Materia()
        mat.nombre = request.POST.get('txtNombre')

        try:
            mat.save()
            parametros['mensaje'] = 'Materia guardada correctamente'
        except Exception as inst:
            parametros['mensaje'] = 'No se puedo guardar la materia'

    return render(request, 'core/materia.html', parametros)

def curso(request, id, nombre):
    cursos = Curso.objects.all().order_by('nombre')
    local = Locacion.objects.filter(institucion=id).order_by('nombre')

    parametros = {
        'local':local,
        'id':id,
        'nombre':nombre
    }

    if request.POST:
        cursos = Curso()

        institucion = Institucion()
        institucion.id = request.POST.get('txtId')
        cursos.institucion = institucion
        cursos.nombre = request.POST.get('txtNombre')
        cursos.duración = request.POST.get('txtDuracion')
        cursos.titulo = request.POST.get('txtTitulo')
        local = Locacion()
        local.id = request.POST.get('cboLocacion')
        cursos.locacion = local

        try:
            cursos.save()
            parametros['mensaje'] = 'Curso guardado correctamente'
        except Exception as e:
            parametros['mensaje'] = 'No se pudo guardar el curso'
        return redirect("institucion", id)

    return render(request, 'core/curso.html', parametros)

def cursoM(request, id, institucion, nombre):
    #Buscamos el curso a modificar
    cursos = Curso.objects.get(id=id)

    local = Locacion.objects.filter(institucion=institucion)
    requisitos = RequisitosCurso.objects.filter(curso=id)
    materias = MateriasCurso.objects.filter(curso=id)

    parametros = {
        'cursos':cursos,
        'local':local,
        'id':id,
        'nombre':nombre,
        'institucion': institucion,
        'requisitos': requisitos,
        'materias': materias
    }

    if request.POST:
        cursos = Curso()
        cursos.id = request.POST.get('txtId')
        institucion = Institucion()
        institucion.id = request.POST.get('txtInstitucion')
        cursos.institucion = institucion
        cursos.nombre = request.POST.get('txtNombre')
        cursos.duración = request.POST.get('txtDuracion')
        cursos.titulo = request.POST.get('txtTitulo')
        local = Locacion()
        local.id = request.POST.get('cboLocacion')
        cursos.locacion = local

        try:
            cursos.save()
            messages.success(request, 'Curso modificado correctamente')
        except:
            messages.error(request, 'No se pudo guardar el curso')
        return redirect("institucion", request.POST.get('txtInstitucion'))

    return render(request, 'core/cursoM.html', parametros)

def verCurso(request, id, nombre):
    #Buscamos el curso a modificar
    cursos = Curso.objects.get(id=id)

    requisitos = RequisitosCurso.objects.filter(curso=id)
    materias = MateriasCurso.objects.filter(curso=id)

    parametros = {
        'cursos':cursos,
        'id':id,
        'nombre':nombre,
        'requisitos': requisitos,
        'materias': materias
    }

    return render(request, 'core/verCurso.html', parametros)

def estudiantes(request, id):
    #Buscamos la institución a cargar
    estudiante = Estudiante.objects.get(id=id)
    seleccion = 'tc'
    condicion = ""

    parametros = {
        'estudiante': estudiante,
        'id':id,
        'seleccion': seleccion,
        'condicion': condicion
    }

    if request.POST:
        stBuscar = request.POST.get('txtBuscar')
        buscar = request.POST.get('cboBuscar')
        buscarN = request.POST.get('cboBuscar.nombre')

        if buscar == "tc":
            cursos = Curso.objects.all()
            parametros = {
                'estudiante': estudiante,
                'cursos':cursos,
                'id':id,
                'seleccion': buscar,
                'condicion': stBuscar
            }
            return render(request, 'core/estudiantes.html', parametros)
        else:
            if stBuscar != "":
                if buscar == 'nc':
                    cursos = Curso.objects.filter(nombre__contains=stBuscar)
                    parametros = {
                        'estudiante': estudiante,
                        'cursos':cursos,
                        'id':id,
                        'seleccion': buscar,
                        'condicion': stBuscar
                    }
                    return render(request, 'core/estudiantes.html', parametros)

                if buscar == 'ci':
                    CursoAux.objects.all().delete()
                    ciudad = Ciudad.objects.filter(nombre__contains=stBuscar)

                    for ci in ciudad:
                        idCi = ci.id
                        locacion = Locacion.objects.filter(ciudad=idCi)
                        for l in locacion:
                            idL = l.id
                            cursoL = Curso.objects.filter(locacion=idL)
                            for cr in cursoL:
                                curso = CursoAux()
                                curso.id = cr.id
                                curso.nombre = cr.nombre
                                curso.duración = cr.duración
                                curso.titulo = cr.titulo
                                curso.save()

                    cursos = CursoAux.objects.all()
                    parametros = {
                        'estudiante': estudiante,
                        'cursos':cursos,
                        'id':id,
                        'seleccion': buscar,
                        'condicion': stBuscar
                    }
                    return render(request, 'core/estudiantes.html', parametros)

                if buscar == 'dc':
                    cursos = Curso.objects.filter(duración__contains=stBuscar)
                    parametros = {
                        'estudiante': estudiante,
                        'cursos':cursos,
                        'id':id,
                        'seleccion': buscar,
                        'condicion': stBuscar
                    }
                    return render(request, 'core/estudiantes.html', parametros)

                if buscar == 'in':
                    CursoAux.objects.all().delete()
                    cursosI = Curso.objects.all()

                    for c in cursosI:
                        curso = CursoAux()
                        curso.id = c.id
                        curso.nombre = c.nombre
                        curso.duración = c.duración
                        curso.titulo = c.titulo
                        curso.institucion = c.institucion.nombre
                        curso.save()

                    cursos = CursoAux.objects.filter(institucion__contains=stBuscar)
                    parametros = {
                        'estudiante': estudiante,
                        'cursos':cursos,
                        'id':id,
                        'seleccion': buscar,
                        'condicion': stBuscar
                    }

                if buscar == 're':
                    CursoAux.objects.all().delete()
                    requisito = Requisito.objects.filter(nombre__contains=stBuscar)

                    for r in requisito:
                        idR = r.id
                        requisitoC = RequisitosCurso.objects.filter(requisito=idR)
                        for rc in requisitoC:
                            idC = rc.curso.id
                            cr = Curso.objects.get(id=idC)
                            curso = CursoAux()
                            curso.id = cr.id
                            curso.nombre = cr.nombre
                            curso.duración = cr.duración
                            curso.titulo = cr.titulo
                            curso.save()

                    cursos = CursoAux.objects.all()
                    parametros = {
                        'estudiante': estudiante,
                        'cursos':cursos,
                        'id':id,
                        'seleccion': buscar,
                        'condicion': stBuscar
                    }
                    return render(request, 'core/estudiantes.html', parametros)

                if buscar == 'tr':
                    cursos = Curso.objects.filter(titulo__contains=stBuscar)
                    parametros = {
                        'estudiante': estudiante,
                        'cursos':cursos,
                        'id':id,
                        'seleccion': buscar,
                        'condicion': stBuscar
                    }
                    return render(request, 'core/estudiantes.html', parametros)

    return render(request, 'core/estudiantes.html', parametros)

def estudiante(request, id):
    #Buscamos el estudiante a modificar
    estudiante = Estudiante.objects.get(id=id)

    niveles = NivelEstudio.objects.all().order_by('nombre')
    paises = Pais.objects.all().order_by('nombre')
    departamentos = Departamento.objects.all().order_by('nombre')
    ciudades = Ciudad.objects.all().order_by('nombre')

    parametros = {
        'estudiante':estudiante,
        'niveles':niveles,
        'paises':paises,
        'departamentos':departamentos,
        'ciudades':ciudades,
    }

    if request.POST:
        estudiante = Estudiante()
        estudiante.id = request.POST.get('txtId')
        estudiante.nombre = request.POST.get('txtNombre')
        pais = Pais()
        pais.id = request.POST.get('cboPais')
        estudiante.pais = pais
        departamento = Departamento()
        departamento.id = request.POST.get('cboDepartamento')
        estudiante.departamento = departamento
        ciudad = Ciudad()
        ciudad.id = request.POST.get('cboCiudad')
        estudiante.ciudad = ciudad
        estudiante.telefono = request.POST.get('txtTelefono')
        estudiante.eMail = request.POST.get('txtMail')
        nivel = NivelEstudio()
        nivel.id = request.POST.get('cboNivel')
        estudiante.nivelEstudio = nivel
        estudiante.usuario = request.POST.get('txtUsuario')
        estudiante.password = request.POST.get('txtPassword')

        try:
            estudiante.save()
            messages.success(request, 'Estudiante modificado correctamente')
        except:
            messages.error(request, 'No se pudo guardar el estudiante')

        return redirect("estudiantes")

    return render(request, 'core/estudiante.html', parametros)

def registroEst(request):
    niveles = NivelEstudio.objects.all().order_by('nombre')
    paises = Pais.objects.all().order_by('nombre')
    departamentos = Departamento.objects.all().order_by('nombre')
    ciudades = Ciudad.objects.all().order_by('nombre')

    parametros = {
        'niveles':niveles,
        'paises':paises,
        'departamentos':departamentos,
        'ciudades':ciudades,
    }

    if request.POST:
        estudiante = Estudiante()
        estudiante.nombre = request.POST.get('txtNombre')
        pais = Pais()
        pais.id = request.POST.get('cboPais')
        estudiante.pais = pais
        departamento = Departamento()
        departamento.id = request.POST.get('cboDepartamento')
        estudiante.departamento = departamento
        ciudad = Ciudad()
        ciudad.id = request.POST.get('cboCiudad')
        estudiante.ciudad = ciudad
        estudiante.telefono = request.POST.get('txtTelefono')
        estudiante.eMail = request.POST.get('txtMail')
        nivel = NivelEstudio()
        nivel.id = request.POST.get('cboNivel')
        estudiante.nivelEstudio = nivel
        estudiante.usuario = request.POST.get('txtUsuario')
        estudiante.password = request.POST.get('txtPassword')

        try:
            estudiante.save()
            parametros['mensaje'] = 'Estudiante guardado correctamente'
        except:
            parametros['mensaje'] = 'No se pudo guardar el estudiante'

    return render(request, 'core/registroEst.html', parametros)

def eliminar_curso(request, id, institucion):
    #Buscar curso a eliminar
    curso = Curso.objects.get(id=id)

    try:
        curso.delete()
        mensaje = "Curso eliminado en forma correcta"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar el curso"
        messages.error(request, mensaje)

    return redirect('institucion', institucion)

def eliminar_locacion(request, id, institucion):
    #Buscar locacion a eliminar
    local = Locacion.objects.get(id=id)

    try:
        local.delete()
        mensaje = "Locacion eliminada en forma correcta"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar la locacion"
        messages.error(request, mensaje)

    return redirect('institucion', institucion)

def eliminar_requisito(request, id, curso, institucion, nombre):
    #Buscar requisito a eliminar
    requisito = RequisitosCurso.objects.get(id=id)

    try:
        requisito.delete()
        mensaje = "Requisito eliminado en forma correcta"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar el requisito"
        messages.error(request, mensaje)

    return redirect('cursoM', curso, institucion, nombre)

def eliminar_materia(request, id, curso, institucion, nombre):
    #Buscar materia a eliminar
    materia = MateriasCurso.objects.get(id=id)

    try:
        materia.delete()
        mensaje = "Materias eliminada en forma correcta"
        messages.success(request, mensaje)
    except:
        mensaje = "No se ha podido eliminar la materia"
        messages.error(request, mensaje)

    return redirect('cursoM', curso, institucion, nombre)
