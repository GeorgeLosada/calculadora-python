import streamlit as st
import math

# Mostrar la imagen del mapa
st.image("mapa_unal.png", caption="Mapa UNAL Bogotá")

# Lista de edificios y sus posiciones en coordenadas (x, y) relativas
edificios = {
    "401 (Geociencias)": (450, 200),
    "421 (Biología)": (500, 230),
    "212 (Ingeniería)": (650, 300),
    "314 (Matemáticas)": (600, 350),
}

comedores = {
    "Comedor Geociencias": (460, 210),
    "Comedor Biología": (510, 240),
    "Comedor Plaza Che": (580, 270),
}

# Seleccionar edificio
opcion = st.selectbox("¿En qué edificio estás?", list(edificios.keys()))

# Calcular distancias
x0, y0 = edificios[opcion]
min_comedor = None
min_dist = float("inf")

for nombre, (x, y) in comedores.items():
    dist = math.hypot(x - x0, y - y0)
    if dist < min_dist:
        min_dist = dist
        min_comedor = nombre

st.success(f"El comedor más cercano es: **{min_comedor}**")
