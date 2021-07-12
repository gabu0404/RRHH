class Cargo:
    def __init__(self):
        self.idCargo = 0
        self.descripcion = ""
        self.area = ""
        self.sueldo = 0.0
        self.estado = 1

    def registrar(self):
        print("Registro del objeto")

    def actualizar(self):
        print("Actualizacion del objeto")

    def eliminar(self):
        print("Eliminacion del objeto")

    def consultar(self):
        print("Consulta de los objetos")