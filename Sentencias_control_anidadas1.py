edad = int(input("Ingresa tu edad"))
if edad < 18:
    print("Ocupas ser mayor de edad para votar")
else: 
    respuesta_credencial = input("¿Tienes credencial para votar? (si/no): ")
    tiene_credencial = respuesta_credencial.lower() == "si"
    if tiene_credencial:
        print("Puedes votar")
    else:
        print("Ocupas credencial para votar")