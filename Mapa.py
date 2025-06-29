import streamlit as st
import math

st.image("maps.png", caption="Mapa UNAL Bogotá")

edificios = {
    # Entradas
    "Portería Calle 26": (120, 480),
    "Portería Capilla": (250, 30),
    "Portería Carrera 45": (600, 480),
    "Portería Calle 53": (840, 100),
    "Portería Hemeroteca": (850, 260),

    # Alrededor Plaza Che
    "104 Auditorio León de Greiff": (390, 260),
    "213 Comedor Ciencias Humanas": (360, 300),
    "224 Edificio Manuel Ancízar": (320, 270),
    "228 Edificio de Enfermería": (340, 310),
    "229 Lenguas Extranjeras": (370, 340),
    "231 Lenguas Extranjeras": (390, 370),
    "212 Aulas de Ciencias Humanas": (400, 290),
    "214 Antonio Nariño (Lingüística / Ing. Civil)": (430, 270),
    "239 Filosofía": (370, 240),
    "225 Posgrados Ciencias Humanas": (310, 300),
    "217 Diseño Gráfico": (410, 250),
    "238 Posgrados Económicas": (420, 320),
    "310 Ciencias Económicas": (450, 350),
    "201 Facultad de Derecho y Ciencias Políticas": (470, 360),

    # Aulas importantes
    "401 Facultad de Ingeniería": (620, 220),
    "404 Matemáticas y Física": (640, 200),
    "405 Posgrados Matemáticas y Física": (660, 190),
    "420 Biología": (700, 250),
    "425 Instituto de Ciencias Naturales": (720, 270),
    "426 Genética": (730, 290),
    "450 Farmacia": (750, 300),
    "451 Química": (760, 320),
    "453 Aulas de Ingeniería": (780, 330),
    "454 Ciencia y Tecnología": (800, 350),
    "476 Facultad de Ciencias": (670, 330),
    "471 Medicina": (680, 310),
    "500 Agrarias": (200, 400),
    "503 Medicina Veterinaria": (220, 420),
    "564 Gloria Galeano (Aulas de Ciencias)": (250, 390),
    "210 Facultad de Odontología": (430, 230),
    "311 Laboratorios de Ing. Mecánica y Eléctrica": (700, 200),
    "412 Laboratorios de Ingeniería Química": (760, 200),
    "314 NEA": (640, 200),
}

comedores = {
    "Comedor Derecho y Ciencias Políticas": (470, 360),
    "Comedor Plaza Che (Central)": (370, 280),
    "Comedor Matemáticas (Takeuchi)": (640, 180),
    "Comedor Hemeroteca": (840, 250),
    "Comedor Geologia": (360, 300),
    "Comedor Economía": (460, 380),
    "Comedor Agrarias": (200, 400),
    "Comedor Ciencias Humanas": (360, 300),
    "Comedor Biología": (200, 400),
    "Comedor Odontología": (430, 240)
}

opcion = st.selectbox("¿En qué edificio estás?", list(edificios.keys()))

# Calcular comedor más cercano
x0, y0 = edificios[opcion]
min_comedor = None
min_dist = float("inf")

for nombre, (x, y) in comedores.items():
    dist = math.hypot(x - x0, y - y0)
    if dist < min_dist:
        min_dist = dist
        min_comedor = nombre

st.success(f"El comedor más cercano es: **{min_comedor}**")
