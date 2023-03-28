class Convertidor:
    def Longitud(self, n1):
        self.n1 = float(n1)
        self.pulgada = self.n1 * 0.39 # Pulgadas
        self.yarda = self.n1 * 0.0109#Yardas
        self.pie = self.n1 * 0.0328#Pies
        self.metro = self.n1 * 0.01#Metros

    def Velocidad(self, n1):
        self.n1 = float(n1)
        self.milla = self.n1 * 0.621371 #millas
        self.metro = self.n1 * 0.277778 #metros
        self.nudo = self.n1 * 0.539957 #nudos
        self.pie = self.n1 * 0.911344 #pie
        
    def Peso(self, n1):
        self.n1 = float(n1)
        self.libra = self.n1 * 2.2046 #libras
        self.onza = self.n1 * 35.2739 #Onzas
        self.tonelada = self.n1 * 0.001 #Toneladas

opcion = 0

while True:
    try:
        n1 = float(input("\nIngrese un número: "))
    except ValueError:
        print("Error: Por favor ingrese un número válido")
        continue
    
    print("""
    Dime, ¿Qué conversión quieres hacer?

    1) Conversión de Longitud
    2) Conversión de Velocidad
    3) Conversión de Peso
    4) Terminar el programa.
    """)
    opcion = int(input("Elige una opción: "))
    
    if opcion == 1:
        cm = Convertidor()
        cm.Longitud(n1)
        print(f'\nLa convercion de {n1}cm es:')
        print(f'{round(cm.pulgada, 2)} pulgadas')
        print(f'{round(cm.yarda, 2)} yardas')
        print(f'{round(cm.pie, 2)} pies')
    
    elif opcion == 2:
        km = Convertidor()
        km.Velocidad(n1)
        print(f'\nLa convercion de {n1}km es:')
        print(f'{round(km.milla, 0)} millas')
        print(f'{round(km.metro, 0)} metros')
        print(f'{round(km.nudo, 0)} nudos')
        print(f'{round(km.pie, 0)} pies')
        print(f'{round(cm.metro, 2)} metros',)
    
    elif opcion == 3:
        kg = Convertidor()
        kg.Peso(n1)
        print(f'\nLa convercion de {n1}kg es')
        print(f'{round(kg.libra, 1)} libras')
        print(f'{round(kg.onza, 1)} onzas')
        print(f'{round(kg.tonelada, 3)} toneladas')

    elif opcion == 4:
        print('\nFin del programa.')
        break
    
    else:
        print("\n Opción incorrecta")
