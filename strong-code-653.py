import streamlit as st

def calcular_pasaje(dias):
    return 3200 * dias

def cuanto_alcanza(plata):
    pasajes = plata // 3200
    sobra = plata % 3200  
    return pasajes, sobra

st.title("Calculadora de Pasajes")

opcion = st.radio("¿Sabe los días que viaja o el dinero con el que cuenta?", ("días", "dinero"))

if opcion == "días":
    dias = st.number_input("Ingrese el número de días", min_value=1, step=1)
    viaje_ida_vuelta = st.radio("¿Ida y vuelta?", ("Sí", "No"))

    if st.button("Calcular costo total"):
        if viaje_ida_vuelta == "Sí":
            total = calcular_pasaje(dias) * 2
        else:
            total = calcular_pasaje(dias)
        st.success(f"Total a pagar: ${total}")

elif opcion == "dinero":
    dinero = st.number_input("Ingrese con cuánto dinero cuenta", min_value=0, step=100)

    if st.button("Calcular número de pasajes"):
        num_pasajes, sobrante = cuanto_alcanza(dinero)
        st.success(f"Número de pasajes: {num_pasajes}")
        st.info(f"Dinero sobrante: ${sobrante}")
