import streamlit as st

def calcular_pasaje(dias):
    return 3200 * dias

def cuanto_alcanza(plata):
    pasajes = plata // 3200
    sobra = plata % 3200
    return pasajes, sobra

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def calcular_grasa(edad, sexo, imc):
    if sexo == "Masculino":
        return 1.20 * imc + 0.23 * edad - 16.2
    else:
        return 1.20 * imc + 0.23 * edad - 5.4


tabs = st.tabs(["Calculadora de Pasajes", "IMC", "% Grasa Corporal"])

with tabs[0]:
    st.header("Calculadora de Pasajes")
    opcion = st.radio("¿Sabe los días o el dinero?", ("días", "dinero"))

    if opcion == "días":
        dias = st.number_input("Número de días", min_value=1, step=1)
        ida_vuelta = st.radio("¿Ida y vuelta?", ("Sí", "No"))
        if st.button("Calcular total"):
            total = calcular_pasaje(dias) * 2 if ida_vuelta == "Sí" else calcular_pasaje(dias)
            st.success(f"Total a pagar: ${total}")

    elif opcion == "dinero":
        dinero = st.number_input("¿Con cuánto dinero cuenta?", min_value=0, step=100)
        if st.button("Calcular pasajes"):
            n, sobrante = cuanto_alcanza(dinero)
            st.success(f"Número de pasajes: {n}")
            st.info(f"Dinero sobrante: ${sobrante}")

with tabs[1]:
    st.header("Calculadora de IMC")
    peso = st.number_input("Peso (kg)", min_value=0.0)
    altura = st.number_input("Altura (m)", min_value=0.0)
    if st.button("Calcular IMC"):
        if altura > 0:
            imc = calcular_imc(peso, altura)
            st.success(f"Tu IMC es {imc:.2f}")
        else:
            st.error("La altura debe ser mayor que 0")

with tabs[2]:
    st.header("Calculadora de Porcentaje de Grasa Corporal")
    edad = st.number_input("Edad", min_value=0)
    sexo = st.radio("Sexo", ["Masculino", "Femenino"])
    imc_grasa = st.number_input("IMC", min_value=0.0)
    if st.button("Calcular % de grasa"):
        grasa = calcular_grasa(edad, sexo, imc_grasa)
        st.success(f"Porcentaje estimado de grasa corporal: {grasa:.2f}%")
