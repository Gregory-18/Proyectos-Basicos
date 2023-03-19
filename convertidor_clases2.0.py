class Convertidor:
    
    def Longitud(self, n1):
        self.n1 = float(n1)
        
        print(f'\nLa convercion de {self.n1}cm es:')
        
        self.pulgada = self.n1 * 0.39 # Pulgadas
        print(f'{round(self.pulgada, 2)} pulgadas')

        self.yarda = self.n1 * 0.0109#Yardas
        print(f'{round(self.yarda, 2)} yardas')

        self.pie = self.n1 * 0.0328#Pies
        print(f'{round(self.pie, 2)} pies')

        self.metro = self.n1 * 0.01#Metros
        print(f'{round(self.metro, 2)} metros',)
    
    def Velocidad(self, n1):
        self.n1 = float(n1)

        print(f'\nLa convercion de {self.n1}km es:')
        
        self.milla = self.n1 * 0.621371 #millas
        print(f'{round(self.milla, 0)} millas')

        self.metro = self.n1 * 0.277778 #metros
        print(f'{round(self.metro, 0)} metros')
        
        self.nudo = self.n1 * 0.539957 #nudos
        print(f'{round(self.nudo, 0)} nudos')
    
        self.pie = self.n1 * 0.911344 #pies
        print(f'{round(self.pie, 0)} pies')
        
    def Peso(self, n1):

        self.n1 = float(n1)

        print(f'\nLa convercion de {self.n1}kg es')
        
        self.libra = self.n1 * 2.2046 #libras
        print(f'{round(self.libra, 1)} libras')

        self.onza = self.n1 * 35.2739 #Onzas
        print(f'{round(self.onza, 1)} onzas')

        self.tonelada = self.n1 * 0.001 #Toneladas
        print(f'{round(self.tonelada, 3)} toneladas')


opcion = 0

while True:
    try:
        n1 = float(input("\nIngrese el primer número: "))
    except ValueError:
        print("Error: Por favor ingrese un número válido")
        continue
    
    print("""
    Dime, ¿Qué conversión quieres hacer?

    1)Conversión de Longitud
    2)Conversión de Velocidad
    3)Conversión de Peso
    4) Terminar el programa.
    """)
    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        cm = Convertidor()
        cm.Longitud(n1)
    
    elif opcion == 2:
        km = Convertidor()
        km.Velocidad(n1)
    
    elif opcion == 3:
        kg = Convertidor()
        kg.Peso(n1)

    elif opcion == 4:
        print('\nFin del programa.')
        break
    
    else:
        print("\n Opción incorrecta")
