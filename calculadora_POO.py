class Calculadora:

    def Suma(self, n1, n2):
        self.n1 = float(n1)
        self.n2 = float(n2)
        self.suma = self.n1 + self.n2
        print(f'\nEl resultado de la suma de {self.n1} + {self.n2} es: {self.suma}')
    
    def Resta(self, n1, n2):
        self.n1 = float(n1)
        self.n2 = float(n2)
        self.resta = self.n1 - self.n2
        print(f'\nEl resultado de la resta de {self.n1} - {self.n2} es: {self.resta}')        
    
    def Multi(self, n1, n2):
        self.n1 = float(n1)
        self.n2 = float(n2)
        self.multi = self.n1 * self.n2
        print(f'\nEl resultado de la multiplicacion de {self.n1} X {self.n2} es: {self.multi}')
    
    def Division(self, n1, n2):
        self.n1 = float(n1)
        self.n2 = float(n2)
        self.divi = self.n1 / self.n2
        print(f'\nEl resultado de la division de {self.n1} ÷ {self.n2} es: {self.divi}')        


opcion = 0

n1 = input('Dime tu primer numero: ')
n2 = input('Dime tu segundo numero: ')
while True:
    print("""
    Dime, ¿qué quieres hacer?

    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Dividir los dos números
    5) Cambiar los números elegidos
    6) Apagar calculadora
    """)
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        sumar = Calculadora()
        sumar.Suma(n1, n2)
    elif opcion == 2:
        restar = Calculadora()
        restar.Resta(n1, n2)
    elif opcion == 3:
        multiplicar = Calculadora()
        multiplicar.Multi(n1, n2)
    elif opcion == 4:
        dividir = Calculadora()
        dividir.Division(n1, n2)
    elif opcion == 5:
        n1 = float(input("Introduce tu primer número: "))
        n2 = float(input("Introduce tu segundo número: "))
    elif opcion == 6:
        break
    else:
        print("Opción incorrecta")
