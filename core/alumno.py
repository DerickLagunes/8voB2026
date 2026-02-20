class alumno:
    ## Instanciar un alumno se ejecuta este código
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def saludar(self):
        return "El alumno {}, te manda un saludo".format(self.nombre)