import typer
from rich import print
from rich.table import Table

#creamos una funcion con el argumento func
def Calculadora(func):#func sera la funcion 
    def vista(*args):
        print(f'Ejecutando la funcion {func.__name__} con los numeros {args}')
        return func(*args)
    return vista

#decorador para que pase los argumentos a Calculadora
@Calculadora
def Suma(n1, n2):
    return n1 + n2
@Calculadora
def Resta(n1, n2):
    return n1 - n2
@Calculadora
def Multiplicacion(n1, n2):
    return n1 * n2
@Calculadora
def Division(n1, n2):
    return n1 / n2

#funcion de Typer
def main():
    print('🤖 [bold green]Por favor ingrese dos numeros[/bold green]')
    
    #Manejo de errores
    def __error():
        try:
            n1 = float(input("Ingrese el primer número: "))
            n2 = float(input("Ingrese el segundo número: "))
            return n1, n2
        except ValueError:
            print("[bold red]Error: Por favor ingrese un número válido.[/bold red]")
            return False

    while True:
        numeros = False
        while not numeros:
            numeros = __error()
        n1,n2 = numeros
        
        print('🤖 [bold green]Calculadora con Decoradores y Typer.[/bold green]')

        #Tabla de informacion
        tabla = Table('Comando', 'Descripcion')
        tabla.add_row('1', 'Sumar')
        tabla.add_row('2', 'Restar')
        tabla.add_row('3', 'Multiplicar')
        tabla.add_row('4', 'Dividir')
        tabla.add_row('5', 'Cambiar los numeros elegidos')
        tabla.add_row('6', 'Apagar la Calculadora')
        print(tabla)
        
        opcion = __confirmacion()

        if opcion == 1:
            print(Suma(n1, n2))        
        elif opcion == 2:
            print(Resta(n1, n2))
        elif opcion == 3:
            print(Multiplicacion(n1, n2))
        elif opcion == 4:
            print(Division(n1, n2))
        elif opcion == 5:
            continue
        else:
            print('[bold red]Opcion no valida.[/bold red]')   

#funcion de confirmacion
def __confirmacion() -> str:
    # definimos la pregunta
    prompt = int(input("\n¿Que opcion quieres realizar? "))

    #confirmacion de salir
    if prompt == 6:
        salir = typer.confirm("🤚 ¿Realmente quieres salir?")
        if salir:
            print('👋 ¡Hasta luego!')
            raise typer.Abort()
        return __confirmacion()
    
    return prompt
    
if __name__ == "__main__":
    typer.run(main)