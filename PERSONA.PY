class Persona:
    nombre = None
    edad = None

    def __init__(self,nombre,edad): 
        self.nombre = nombre
        self.edad = edad

    def mostrar(self):
        return f"{self.nombre},edad :{self.edad}"
class Empleado(Persona):
    sueldo_bruto= None

    def __init__(self, nombre, edad,sueldo):
        super().__init__(nombre, edad)
        self.sueldo_bruto= sueldo

    def mostrar(self):
        return super().mostrar()+ f"SN: {self.calcular_salario_neto()}"
    
    def calcular_salario_neto(self):
        return self.sueldo_bruto * 0.9 
    
    class Cliente(Persona):
        def __init__(self, nombre, edad, numero_de_telefono):
            super().__init__(nombre, edad)
            self.contacto= numero_de_telefono
        def mostrar(self):
            return super().mostrar()+ f'el contacto del cliente es: {self.contacto}'

        


    class Directivo():
        pass


    class Empresa():

        if __name__== "__main__":
         persona= Empleado('gabriel',19,1200)
        print(persona.mostrar())
        
        