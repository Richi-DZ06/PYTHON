class Calculadora:
    numero1= None
    numero2= None
    resultado= None
    historial= None

    def __init__(self,n,m):
        self.numero1=n
        self.numero2=m
        self.resultado=0
        historial=[]

    def sumar(self):
        return self.numero1+ self.numero2
    def restar(self):
        return self.numero1- self.numero2
    def set_numeros(self,x,y):
        self.numero1= x
        self.numero2= y
    
    

if __name__ == "__main__":
    casio = Calculadora (45,50)
    casio2 = Calculadora (96,85)
    print("suma: ",casio.sumar())
    print("resta: ",casio.restar())
   
    casio 
