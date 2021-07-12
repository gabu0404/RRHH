class RolPago:
    def __init__(self):
        self.idRolPago = 0
        self.descripcion = ""
        self.mes = ""
        self.año = ""
        self.fechaPago = ""
        self.monto = 0.0
        self.tipoPago = ""
        self.cuentaDebito = ""
        self.estado = 1

    def registrar(self):
        print("Registro del objeto")

    def actualizar(self):
        print("Actualizacion del objeto")

    def eliminar(self):
        print("Eliminacion del objeto")

    def consultar(self):
        print("Consulta de los objetos")