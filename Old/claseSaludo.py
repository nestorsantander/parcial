class Saludo:
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def decir_hola(self):
        if self.mensaje == "hola":
            print("Hola mundo")
        else:
            print("error")

