numero = int(input("Introduce un numero para ver su tabla de multiplicar"))
for i in range(1, 11):
    resultado = numero * i 
    print(f"{numero} x {i} = {resultado}")
