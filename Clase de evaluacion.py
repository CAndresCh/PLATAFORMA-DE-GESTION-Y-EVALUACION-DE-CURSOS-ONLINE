# CLASE BASE DE EVALUACIÓN

class Evaluacion:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso
        self.notas = {}  # {estudiante: nota}

    def asignar_nota(self, estudiante, nota):
        if estudiante not in self.curso.estudiantes_inscritos:
            raise ValueError(f"El estudiante {estudiante.nombre} no está inscrito en {self.curso.nombre}")
        self.notas[estudiante] = nota
        estudiante.asignar_calificacion(self.curso, nota)

    def __str__(self):
        return f"Evaluación: {self.nombre}"
