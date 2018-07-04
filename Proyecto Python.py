#primero lanzar los dados y segun el numero que saque se elegirá al jugador x en la lista, después a este se le aplica el random para decidir si queda fuera o no

from random import randint
from time import sleep

def Select(x,y):
    if len(x)!=1:
        if len(x)==y:
            return x[y-1]
        elif len(x)>y:
            return x[y-1]
        elif y>len(x):
            while y>len(x):
                y=y-len(x)
            return x[y-1]
    else:
        return "Queda 1"

def IfKill(x,y):
    if Select(x,y)!="Queda 1":
        k=randint(0,1)
        if k==1:
            a=Select(x,y)
            x.remove(Select(x,y))
            print(f"¡El/La jugador{a} ha sido eliminad@!")
            print("Suerte para la próxima ;)")
            return "ELIMINAD@"
        else:
            a = Select(x, y)
            print(f"¡El/La jugador@ {a} se ha salvado!")
            return "SALVAD@"
    else:
        print("1 jugador/a restante...")
        return "NO ELIMINAR"

def Main(x,y):
    while len(x)!=1:
        print(f"Se ha seleccionado al jugador {Select(x,y)}")
        print("UYUYUY....!")

    return f"¡EL JUGADOR {x[0]} GANA!"


Main(input().split(","),randint(1,6))
