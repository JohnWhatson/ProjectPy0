# ProjectPy0
#Proyecto grupal de Python, ICC

#fibonacci n' shit! xd

def SumaFibonacci(x):
    numeros=[0]
    for i in range(x):
        if len(numeros)==1:
            numeros.append(1)
        else:
            numeros.append(numeros[-1]+numeros[-2])
        print(numeros[i])

print(SumaFibonacci(int(input())))
