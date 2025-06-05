import streamlit as st
import numpy as np
import pandas as pd

def producto_por_escalar(matriz, escalar):
    return matriz * escalar

def suma_matrices(m1, m2):
    return m1 + m2

def resta_matrices(m1, m2):
    return m1 - m2

def multiplicacion_elemento(m1, m2):
    return m1 * m2

def suma_diagonal(matriz):
    return np.trace(matriz)

def menor_valor(matriz):
    return matriz.min()

def mayor_valor(matriz):
    return matriz.max()

def suma_total(matriz):
    return matriz.sum()

def promedio_matriz(matriz):
    return int(matriz.mean())

def multiplicacion_matricial(m1, m2):
    return np.dot(m1, m2)

st.set_page_config(layout="wide")
st.title("🔢 Calculadora de Matrices - George Losada")

filas = st.sidebar.number_input("Número de filas", 1, 10, value=3)
columnas = st.sidebar.number_input("Número de columnas", 1, 10, value=3)

if "A_df" not in st.session_state or st.session_state["A_df"].shape != (filas, columnas):
    st.session_state["A_df"] = pd.DataFrame(np.zeros((filas, columnas), dtype=int))

if "B_df" not in st.session_state or st.session_state["B_df"].shape != (filas, columnas):
    st.session_state["B_df"] = pd.DataFrame(np.zeros((filas, columnas), dtype=int))

st.subheader("🔧 Matriz A - Personalizada")
A_df = st.data_editor(st.session_state["A_df"], num_rows="dynamic", use_container_width=True)
A = A_df.to_numpy()
st.session_state["A_df"] = A_df

st.subheader("🔧 Matriz B - Personalizada")
B_df = st.data_editor(st.session_state["B_df"], num_rows="dynamic", use_container_width=True)
B = B_df.to_numpy()
st.session_state["B_df"] = B_df

opcion = st.sidebar.selectbox("Seleccione una operación:", [
    "Ver matrices A y B",
    "Producto por escalar",
    "Suma de matrices",
    "Resta de matrices",
    "Multiplicación elemento a elemento",
    "Suma diagonal de A",
    "Menor valor de A",
    "Mayor valor de A",
    "Suma total de A",
    "Promedio de A",
    "Multiplicación matricial"
])

if opcion == "Ver matrices A y B":
    st.subheader("Matriz A")
    st.dataframe(A)
    st.subheader("Matriz B")
    st.dataframe(B)

elif opcion == "Producto por escalar":
    escalar = st.sidebar.number_input("Ingrese escalar", value=2)
    resultado = producto_por_escalar(A, escalar)
    st.write(f"Matriz A * {escalar}:")
    st.dataframe(resultado)

elif opcion == "Suma de matrices":
    resultado = suma_matrices(A, B)
    st.write("A + B:")
    st.dataframe(resultado)

elif opcion == "Resta de matrices":
    resultado = resta_matrices(A, B)
    st.write("A - B:")
    st.dataframe(resultado)

elif opcion == "Multiplicación elemento a elemento":
    resultado = multiplicacion_elemento(A, B)
    st.write("A * B (elemento a elemento):")
    st.dataframe(resultado)

elif opcion == "Suma diagonal de A":
    if A.shape[0] == A.shape[1]:
        st.write(f"Suma de la diagonal de A: {suma_diagonal(A)}")
    else:
        st.warning("La matriz A no es cuadrada.")

elif opcion == "Menor valor de A":
    st.write(f"Menor valor en A: {menor_valor(A)}")

elif opcion == "Mayor valor de A":
    st.write(f"Mayor valor en A: {mayor_valor(A)}")

elif opcion == "Suma total de A":
    st.write(f"Suma total de A: {suma_total(A)}")

elif opcion == "Promedio de A":
    st.write(f"Promedio de A: {promedio_matriz(A)}")

elif opcion == "Multiplicación matricial":
    if A.shape[1] != B.shape[0]:
        st.warning("No se puede multiplicar: columnas de A distintas de filas de B.")
    else:
        resultado = multiplicacion_matricial(A, B)
        st.write("A * B (matricial):")
        st.dataframe(resultado)
