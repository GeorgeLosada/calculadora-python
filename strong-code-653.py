def calcular_pasaje(dias):
    return 3200 * dias
    
def cuanto_alcanza(plata):
    pasajes = plata // 3200
    sobra = plata % 3200  
    return pasajes, sobra

tipo = input("¿Sabe los días que viaja o el dinero con el que cuenta? (dias/dinero): ").lower()

if tipo == "dias":
    dias = int(input("Ingrese el número de días: "))
    viaje = input("¿Ida y vuelta? (s/n): ").lower()
    
    if viaje == 's':
        print(f"Total a pagar: ${calcular_pasaje(dias) * 2}")
    elif viaje == 'n':
        print(f"Total a pagar: ${calcular_pasaje(dias)}")
    else:
        print("Error: Responda 's' o 'n'")

elif tipo == "dinero":
    dinero = int(input("Ingrese con cuánto dinero cuenta: "))
    num_pasajes, sobrante = cuanto_alcanza(dinero)
    print(f"Número de pasajes: {num_pasajes}")
    print(f"Dinero sobrante: ${sobrante}")
else:
    print("Error: Responda 'dias' o 'dinero'")