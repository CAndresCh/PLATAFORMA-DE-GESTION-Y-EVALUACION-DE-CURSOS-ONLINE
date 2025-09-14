# USUARIO (hereda a estudiante e instructor)
class Usuario:
    def __init__(self, id_usuario, nombre, email):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        
    def __str__(self):
        return (
            f"--- BIENVENIDO USUARIO ---\n"
            f" - Nombre de usuario: {self.nombre}\n"
            f" - Id de usuario: {self.id_usuario}\n"
            f" - Correo electrónico de usuario: {self.email}"
        )

# Clase Estudiante
class Estudiante(Usuario):
    def __init__(self, id_usuario, nombre, email):
        super().__init__(id_usuario, nombre, email)
        self.cursos_inscritos = []
        self.calificaciones = {}

    def inscribir_curso(self, curso):
        if curso in self.cursos_inscritos:
            raise ValueError(f"El estudiante {self.nombre}, ya está inscrito en este curso")
        self.cursos_inscritos.append(curso)
        print(f"Estudiante: {self.nombre}, ha sido inscrito en el curso: {curso.nombre}")

    def asignar_calificacion(self, curso, nota):
        if curso not in self.cursos_inscritos:
            raise ValueError(f"No se puede asignar nota, el estudiante no está inscrito en: {curso.nombre}")
        self.calificaciones[curso.nombre] = nota
        print(f"Nota asignada en {curso.nombre}: {nota}")

    def obtener_cursos_inscritos(self):
        return [curso.nombre for curso in self.cursos_inscritos]

    def __str__(self):
        cursos = ', '.join(self.obtener_cursos_inscritos()) if self.cursos_inscritos else "Ninguno"
        calificaciones = (
            '\n'.join([f" °-° {curso}: {nota}" for curso, nota in self.calificaciones.items()])
            if self.calificaciones else "   - Sin calificaciones registradas"
        )
        return (
            super().__str__() + "\n"
            f" - Cursos inscritos: {cursos}\n"
            f" - Calificaciones:\n{calificaciones}"
        )
# Clase Instructor
class Instructor(Usuario):
    def __init__(self, id_usuario, nombre, email):
        super().__init__(id_usuario, nombre, email)
        self.cursos_impartidos = []

    def agregar_curso(self, curso):
        self.cursos_impartidos.append(curso)
        print(f"Curso {curso.nombre} agregado al instructor {self.nombre}")

    def obtener_cursos_impartidos(self):
        return [curso.nombre for curso in self.cursos_impartidos]

    def __str__(self):
        cursos = ', '.join(self.obtener_cursos_impartidos()) if self.cursos_impartidos else "Ninguno"
        return (
            super().__str__() + "\n"
            f" - Cursos impartidos: {cursos}"
        )





# CUURSO (hereda a evalucacion)
class Curso:
    def __init__(self, codigo, nombre, instructor):
        self.codigo = codigo
        self.nombre = nombre
        self.instructor = instructor
        self.estudiantes_inscritos = []
        self.evaluaciones = []

    def inscribir_estudiante(self, estudiante):
        if estudiante in self.estudiantes_inscritos:
            print(f"El estudiante {estudiante.nombre} ya está inscrito en el curso {self.nombre}.")
            return
        try:
            estudiante.inscribir_curso(self)
            self.estudiantes_inscritos.append(estudiante)
        except ValueError as e:
            print(f"Error al inscribir estudiante: {e}")

    def crear_evaluacion(self, evaluacion):
        if any(ev.nombre == evaluacion.nombre for ev in self.evaluaciones):
            print(f"Ya existe una evaluación llamada '{evaluacion.nombre}' en este curso.")
            return
        self.evaluaciones.append(evaluacion)
        print(f"Evaluación {evaluacion.nombre} creada para el curso: {self.nombre}")

    def mostrar_info_completa(self):
        print(f"\n--- INFORMACIÓN DEL CURSO ---")
        print(f" - Código: {self.codigo}")
        print(f" - Nombre: {self.nombre}")
        print(f" - Instructor: {self.instructor.nombre}")
        print(f" - Estudiantes inscritos:")
        if self.estudiantes_inscritos:
            for est in self.estudiantes_inscritos:
                print(f"    - {est.nombre} (ID: {est.id_usuario})")
        else:
            print("    - Ninguno")
        print(f" - Evaluaciones creadas:")
        if self.evaluaciones:
            for ev in self.evaluaciones:
                print(f"    - {str(ev)}")
        else:
            print("    - Ninguna")

class Evaluacion:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo  

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"




# PLATAFORMA
class Plataforma:
    def __init__(self):
        self.usuarios = {}
        self.cursos = {}
        
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            raise ValueError("ID de usuario ya existe.")
        self.usuarios[usuario.id_usuario] = usuario
        print(f"Usuario {usuario.nombre} registrado con éxito.")

    def crear_curso(self, codigo, nombre, id_instructor):
        if id_instructor not in self.usuarios or not isinstance(self.usuarios[id_instructor], Instructor):
            raise ValueError("Instructor no válido o no encontrado.")
        
        instructor = self.usuarios[id_instructor]
        nuevo_curso = Curso(codigo, nombre, instructor)
        self.cursos[codigo] = nuevo_curso
        instructor.agregar_curso(nuevo_curso)

    def inscribir_estudiante_en_curso(self, id_estudiante, codigo_curso):
        estudiante = self.usuarios.get(id_estudiante)
        curso = self.cursos.get(codigo_curso)
        
        if not isinstance(estudiante, Estudiante):
            print("ID de usuario no corresponde a un estudiante.")
            return
        if not curso:
            print("Código de curso no encontrado.")
            return
        
        curso.inscribir_estudiante(estudiante)

    def obtener_info_curso(self, codigo_curso):
        return self.cursos.get(codigo_curso)



# VALIDACIONES
def pedir_id():
    while True:
        id_usuario = input("Ingrese el ID (solo números): ")
        if id_usuario.isdigit():
            return int(id_usuario)
        print("Error: El ID debe contener solo números.")

def pedir_nombre():
    while True:
        nombre = input("Ingrese el nombre (sin números): ")
        if nombre.replace(" ", "").isalpha():
            return nombre
        print("Error: El nombre no debe contener números ni símbolos.")

def pedir_email():
    while True:
        email = input("Ingrese el correo electrónico: ")
        if "@" in email and "." in email:
            return email
        print("Error: El correo debe contener '@' y '.'")

def pedir_codigo():
    while True:
        codigo = input("Ingrese el código del curso (solo números): ")
        if codigo.isdigit():
            return int(codigo)
        print("Error: El código debe contener solo números.")

def pedir_nombre_curso():
    while True:
        nombre = input("Ingrese el nombre del curso (sin números): ")
        if nombre.replace(" ", "").isalpha():
            return nombre
        print("Error: El nombre no debe contener números ni símbolos.")

def pedir_nombre_evaluacion():
    while True:
        nombre = input("Ingrese el nombre de la evaluación: ")
        if nombre.strip():
            return nombre
        print("Error: El nombre no puede estar vacío.")

def pedir_tipo_evaluacion():
    while True:
        tipo = input("Ingrese el tipo de evaluación (Ej: Examen, Proyecto, Tarea): ")
        if tipo.replace(" ", "").isalpha():
            return tipo
        print("Error: El tipo debe contener solo letras.")



# MENU
def menu_principal(plataforma):
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Registrar nuevo usuario")
        print("2. Acceder como usuario existente")
        print("3. Crear curso")
        print("4. Inscribir estudiante en curso")
        print("5. Crear evaluación")
        print("6. Mostrar información de curso")
        print("7. Mostrar todos los usuarios")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("¿Es Estudiante (E) o Instructor (I)? ").strip().upper()
            id_usuario = pedir_id()
            if id_usuario in plataforma.usuarios:
                print("Ya existe un usuario con ese ID. Use la opción 2 para acceder.")
                continue
            nombre = pedir_nombre()
            email = pedir_email()
            if tipo == "E":
                usuario = Estudiante(id_usuario, nombre, email)
            elif tipo == "I":
                usuario = Instructor(id_usuario, nombre, email)
            else:
                print("Tipo no válido.")
                continue

            plataforma.registrar_usuario(usuario)

        elif opcion == "2":
            id_usuario = pedir_id()
            usuario = plataforma.usuarios.get(id_usuario)
            if usuario:
                print("\n--- USUARIO ENCONTRADO ---")
                print(usuario)
            else:
                print("Usuario no encontrado. Regístrese primero.")

        elif opcion == "3":
            codigo = pedir_codigo()
            nombre = pedir_nombre_curso()
            id_instructor = pedir_id()
            try:
                plataforma.crear_curso(codigo, nombre, id_instructor)
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == "4":
            id_estudiante = pedir_id()
            codigo_curso = pedir_codigo()
            plataforma.inscribir_estudiante_en_curso(id_estudiante, codigo_curso)

        elif opcion == "5":
            codigo_curso = pedir_codigo()
            curso = plataforma.obtener_info_curso(codigo_curso)
            if curso:
                nombre_eval = pedir_nombre_evaluacion()
                tipo_eval = pedir_tipo_evaluacion()
                evaluacion = Evaluacion(nombre_eval, tipo_eval)
                curso.crear_evaluacion(evaluacion)
            else:
                print("Curso no encontrado.")

        elif opcion == "6":
            codigo_curso = pedir_codigo()
            curso = plataforma.obtener_info_curso(codigo_curso)
            if curso:
                curso.mostrar_info_completa()
            else:
                print("Curso no encontrado.")

        elif opcion == "7":
            print("\n--- LISTA DE USUARIOS REGISTRADOS ---")
            for u in plataforma.usuarios.values():
                print(u)
                print("-" * 40)

        elif opcion == "8":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")

# INSTANCIA GENERAL
plataforma = Plataforma()
menu_principal(plataforma)
