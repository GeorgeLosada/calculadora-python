import streamlit as st
import pandas as pd
import re

st.title("Verificador de Doble Titulación - Departamento de Matemáticas UNAL")

# --- Cargar mallas curriculares (simplificadas) ---
MALLAS = {
    "Matemáticas": {
        "Cálculo I": 4, "Álgebra Lineal": 4, "Fundamentos de Matemáticas": 4, "Ecuaciones Diferenciales": 3,
        "Cálculo II": 4, "Análisis Real": 4, "Álgebra Abstracta": 4
    },
    "Física": {
        "Cálculo I": 4, "Física I": 4, "Física II": 4, "Álgebra Lineal": 4, "Electromagnetismo": 4
    },
    "Estadística": {
        "Probabilidad I": 4, "Estadística I": 4, "Cálculo I": 4, "Álgebra Lineal": 4, "Programación": 3
    },
    "Ciencias de la Computación": {
        "Programación I": 4, "Estructuras de Datos": 4, "Álgebra Lineal": 4, "Cálculo I": 4, "Teoría de la Computación": 3
    }
}

# --- Funciones ---
def parse_historia(txt):
    materias = {}
    total_cred_aprob = 0
    suma_puntos = 0
    total_materias = 0
    for line in txt.splitlines():
        match = re.match(r"(.+?)\s+-\s+([0-5]\.?\d*)\s+-\s+(\d+)", line)
        if match:
            nombre, nota, creditos = match.groups()
            nota = float(nota)
            creditos = int(creditos)
            materias[nombre.strip()] = (nota, creditos)
            if nota >= 3.0:
                total_cred_aprob += creditos
            suma_puntos += nota * creditos
            total_materias += creditos
    papa = suma_puntos / total_materias if total_materias > 0 else 0
    return materias, total_cred_aprob, papa

def evaluar_doble_titulacion(materias, total_cred, papa):
    estado = {}
    for carrera, malla in MALLAS.items():
        if carrera == "Matemáticas":
            continue
        homologadas = []
        faltantes = []
        total_malla = sum(malla.values())
        for mat, cred in malla.items():
            if mat in materias and materias[mat][0] >= 3.0:
                homologadas.append(mat)
            else:
                faltantes.append(mat)
        cumple_creditos = total_cred >= 0.4 * 140  # Supongamos que Matemáticas tiene 140 créditos
        cumple_papa = papa >= 3.0
        if cumple_creditos and cumple_papa:
            estado[carrera] = {
                "Estado": "✔ Cumple requisitos",
                "Homologadas": homologadas,
                "Faltantes": faltantes,
                "Créditos homologados": sum([malla[m] for m in homologadas]),
                "Créditos faltantes": sum([malla[m] for m in faltantes])
            }
        elif cumple_creditos:
            estado[carrera] = {"Estado": "❌ No cumple con el PAPA (mínimo 3.0)"}
        else:
            estado[carrera] = {"Estado": "❌ No cumple con los créditos (mínimo 40% del primer plan)"}
    return estado

# --- Interfaz ---
archivo = st.file_uploader("Sube tu historia académica (.txt)", type="txt")

if archivo:
    texto = archivo.read().decode("utf-8")
    materias, total_cred, papa = parse_historia(texto)

    st.write(f"**Total créditos aprobados:** {total_cred}")
    st.write(f"**PAPA:** {papa:.2f}")

    resultado = evaluar_doble_titulacion(materias, total_cred, papa)

    for carrera, info in resultado.items():
        st.subheader(carrera)
        st.write(f"**Estado:** {info['Estado']}")
        if "Homologadas" in info:
            st.write(f"**Materias homologadas:** {', '.join(info['Homologadas'])}")
            st.write(f"**Materias faltantes:** {', '.join(info['Faltantes'])}")
            st.write(f"**Créditos homologados:** {info['Créditos homologados']} / {info['Créditos homologados'] + info['Créditos faltantes']}")
