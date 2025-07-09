import streamlit as st
import pandas as pd
from datetime import time

# Datos completos de monitorías por materia
monitorias = [
    # Álgebra Lineal
    {"Materia": "Álgebra Lineal", "Día": "LUNES", "Hora Inicio": time(7,0), "Hora Fin": time(8,0)},
    {"Materia": "Álgebra Lineal", "Día": "LUNES", "Hora Inicio": time(8,0), "Hora Fin": time(9,0)},
    {"Materia": "Álgebra Lineal", "Día": "LUNES", "Hora Inicio": time(9,0), "Hora Fin": time(10,0)},
    {"Materia": "Álgebra Lineal", "Día": "LUNES", "Hora Inicio": time(10,0), "Hora Fin": time(11,0)},
    {"Materia": "Álgebra Lineal", "Día": "LUNES", "Hora Inicio": time(11,0), "Hora Fin": time(12,0)},
    {"Materia": "Álgebra Lineal", "Día": "LUNES", "Hora Inicio": time(12,0), "Hora Fin": time(13,0)},
    {"Materia": "Álgebra Lineal", "Día": "LUNES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0)},
    {"Materia": "Álgebra Lineal", "Día": "LUNES", "Hora Inicio": time(16,0), "Hora Fin": time(17,0)},
    
    {"Materia": "Álgebra Lineal", "Día": "MARTES", "Hora Inicio": time(7,0), "Hora Fin": time(8,0)},
    {"Materia": "Álgebra Lineal", "Día": "MARTES", "Hora Inicio": time(8,0), "Hora Fin": time(9,0)},
    {"Materia": "Álgebra Lineal", "Día": "MARTES", "Hora Inicio": time(14,0), "Hora Fin": time(15,0)},
    {"Materia": "Álgebra Lineal", "Día": "MARTES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0)},
    {"Materia": "Álgebra Lineal", "Día": "MARTES", "Hora Inicio": time(16,0), "Hora Fin": time(17,0)},
    {"Materia": "Álgebra Lineal", "Día": "MARTES", "Hora Inicio": time(17,0), "Hora Fin": time(18,0)},
    
    {"Materia": "Álgebra Lineal", "Día": "MIERCOLES", "Hora Inicio": time(7,0), "Hora Fin": time(8,0)},
    {"Materia": "Álgebra Lineal", "Día": "MIERCOLES", "Hora Inicio": time(8,0), "Hora Fin": time(9,0)},
    {"Materia": "Álgebra Lineal", "Día": "MIERCOLES", "Hora Inicio": time(9,0), "Hora Fin": time(10,0)},
    {"Materia": "Álgebra Lineal", "Día": "MIERCOLES", "Hora Inicio": time(10,0), "Hora Fin": time(11,0)},
    {"Materia": "Álgebra Lineal", "Día": "MIERCOLES", "Hora Inicio": time(11,0), "Hora Fin": time(12,0)},
    {"Materia": "Álgebra Lineal", "Día": "MIERCOLES", "Hora Inicio": time(12,0), "Hora Fin": time(13,0)},
    {"Materia": "Álgebra Lineal", "Día": "MIERCOLES", "Hora Inicio": time(14,0), "Hora Fin": time(15,0)},
    {"Materia": "Álgebra Lineal", "Día": "MIERCOLES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0)},
    
    {"Materia": "Álgebra Lineal", "Día": "JUEVES", "Hora Inicio": time(7,0), "Hora Fin": time(8,0)},
    {"Materia": "Álgebra Lineal", "Día": "JUEVES", "Hora Inicio": time(8,0), "Hora Fin": time(9,0)},
    {"Materia": "Álgebra Lineal", "Día": "JUEVES", "Hora Inicio": time(9,0), "Hora Fin": time(10,0)},
    {"Materia": "Álgebra Lineal", "Día": "JUEVES", "Hora Inicio": time(10,0), "Hora Fin": time(11,0)},
    {"Materia": "Álgebra Lineal", "Día": "JUEVES", "Hora Inicio": time(14,0), "Hora Fin": time(15,0)},
    {"Materia": "Álgebra Lineal", "Día": "JUEVES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0)},
    
    {"Materia": "Álgebra Lineal", "Día": "VIERNES", "Hora Inicio": time(7,0), "Hora Fin": time(8,0)},
    {"Materia": "Álgebra Lineal", "Día": "VIERNES", "Hora Inicio": time(8,0), "Hora Fin": time(9,0)},
    {"Materia": "Álgebra Lineal", "Día": "VIERNES", "Hora Inicio": time(11,0), "Hora Fin": time(12,0)},
    {"Materia": "Álgebra Lineal", "Día": "VIERNES", "Hora Inicio": time(12,0), "Hora Fin": time(13,0)},
    
    # Cálculo Diferencial
    {"Materia": "Cálculo Diferencial", "Día": "MARTES", "Hora Inicio": time(7,0), "Hora Fin": time(8,0)},
    {"Materia": "Cálculo Diferencial", "Día": "MARTES", "Hora Inicio": time(8,0), "Hora Fin": time(9,0)},
    {"Materia": "Cálculo Diferencial", "Día": "MIERCOLES", "Hora Inicio": time(9,0), "Hora Fin": time(10,0)},
    {"Materia": "Cálculo Diferencial", "Día": "MIERCOLES", "Hora Inicio": time(10,0), "Hora Fin": time(11,0)},
    {"Materia": "Cálculo Diferencial", "Día": "MIERCOLES", "Hora Inicio": time(11,0), "Hora Fin": time(12,0)},
    {"Materia": "Cálculo Diferencial", "Día": "JUEVES", "Hora Inicio": time(7,0), "Hora Fin": time(8,0)},
    {"Materia": "Cálculo Diferencial", "Día": "JUEVES", "Hora Inicio": time(8,0), "Hora Fin": time(9,0)},
    {"Materia": "Cálculo Diferencial", "Día": "VIERNES", "Hora Inicio": time(9,0), "Hora Fin": time(10,0)},
    {"Materia": "Cálculo Diferencial", "Día": "VIERNES", "Hora Inicio": time(17,0), "Hora Fin": time(18,0)},
    {"Materia": "Cálculo Diferencial", "Día": "VIERNES", "Hora Inicio": time(18,0), "Hora Fin": time(19,0)},
    {"Materia": "Cálculo Diferencial", "Día": "MARTES", "Hora Inicio": time(14,0), "Hora Fin": time(15,0)},
    {"Materia": "Cálculo Diferencial", "Día": "MARTES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0)},
    {"Materia": "Cálculo Diferencial", "Día": "JUEVES", "Hora Inicio": time(14,0), "Hora Fin": time(15,0)},
    {"Materia": "Cálculo Diferencial", "Día": "JUEVES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0)},
    {"Materia": "Cálculo Diferencial", "Día": "JUEVES", "Hora Inicio": time(16,0), "Hora Fin": time(17,0)},
    
    # Cálculo Integral
    {"Materia": "Cálculo Integral", "Día": "LUNES", "Hora Inicio": time(9,0), "Hora Fin": time(10,0)},
    {"Materia": "Cálculo Integral", "Día": "LUNES", "Hora Inicio": time(10,0), "Hora Fin": time(11,0)},
    {"Materia": "Cálculo Integral", "Día": "MARTES", "Hora Inicio": time(9,0), "Hora Fin": time(10,0)},
    {"Materia": "Cálculo Integral", "Día": "MARTES", "Hora Inicio": time(11,0), "Hora Fin": time(12,0)},
    {"Materia": "Cálculo Integral", "Día": "MARTES", "Hora Inicio": time(12,0), "Hora Fin": time(13,0)},
    {"Materia": "Cálculo Integral", "Día": "MIERCOLES", "Hora Inicio": time(11,0), "Hora Fin": time(12,0)},
    {"Materia": "Cálculo Integral", "Día": "MIERCOLES", "Hora Inicio": time(12,0), "Hora Fin": time(13,0)},
    {"Materia": "Cálculo Integral", "Día": "JUEVES", "Hora Inicio": time(11,0), "Hora Fin": time(12,0)},
    {"Materia": "Cálculo Integral", "Día": "JUEVES", "Hora Inicio": time(12,0), "Hora Fin": time(13,0)},
    {"Materia": "Cálculo Integral", "Día": "VIERNES", "Hora Inicio": time(11,0), "Hora Fin": time(12,0)},
    {"Materia": "Cálculo Integral", "Día": "VIERNES", "Hora Inicio": time(12,0), "Hora Fin": time(13,0)},
    {"Materia": "Cálculo Integral", "Día": "LUNES", "Hora Inicio": time(14,0), "Hora Fin": time(15,0)},
    {"Materia": "Cálculo Integral", "Día": "MIERCOLES", "Hora Inicio": time(14,0), "Hora Fin": time(15,0)},
    {"Materia": "Cálculo Integral", "Día": "JUEVES", "Hora Inicio": time(14,0), "Hora Fin": time(15,0)},
    {"Materia": "Cálculo Integral", "Día": "MARTES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0)},
    {"Materia": "Cálculo Integral", "Día": "MIERCOLES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0)},
    {"Materia": "Cálculo Integral", "Día": "JUEVES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0)},
    
    # Cálculo en Varias Variables
    {"Materia": "Cálculo en Varias Variables", "Día": "LUNES", "Hora Inicio": time(7,0), "Hora Fin": time(8,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "LUNES", "Hora Inicio": time(8,0), "Hora Fin": time(9,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "LUNES", "Hora Inicio": time(11,0), "Hora Fin": time(12,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "LUNES", "Hora Inicio": time(12,0), "Hora Fin": time(13,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "MARTES", "Hora Inicio": time(7,0), "Hora Fin": time(8,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "MARTES", "Hora Inicio": time(8,0), "Hora Fin": time(9,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "MARTES", "Hora Inicio": time(11,0), "Hora Fin": time(12,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "MARTES", "Hora Inicio": time(12,0), "Hora Fin": time(13,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "MIERCOLES", "Hora Inicio": time(7,0), "Hora Fin": time(8,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "MIERCOLES", "Hora Inicio": time(8,0), "Hora Fin": time(9,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "MIERCOLES", "Hora Inicio": time(9,0), "Hora Fin": time(10,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "MIERCOLES", "Hora Inicio": time(10,0), "Hora Fin": time(11,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "JUEVES", "Hora Inicio": time(7,0), "Hora Fin": time(8,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "JUEVES", "Hora Inicio": time(8,0), "Hora Fin": time(9,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "JUEVES", "Hora Inicio": time(11,0), "Hora Fin": time(12,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "JUEVES", "Hora Inicio": time(12,0), "Hora Fin": time(13,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "VIERNES", "Hora Inicio": time(7,0), "Hora Fin": time(8,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "VIERNES", "Hora Inicio": time(8,0), "Hora Fin": time(9,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "MARTES", "Hora Inicio": time(14,0), "Hora Fin": time(15,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "JUEVES", "Hora Inicio": time(14,0), "Hora Fin": time(15,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "VIERNES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "MIERCOLES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "MIERCOLES", "Hora Inicio": time(16,0), "Hora Fin": time(17,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "MARTES", "Hora Inicio": time(16,0), "Hora Fin": time(18,0)},
    {"Materia": "Cálculo en Varias Variables", "Día": "VIERNES", "Hora Inicio": time(16,0), "Hora Fin": time(18,0)},
    
    # Ecuaciones Diferenciales
    {"Materia": "Ecuaciones Diferenciales", "Día": "MIERCOLES", "Hora Inicio": time(7,0), "Hora Fin": time(8,0)},
    {"Materia": "Ecuaciones Diferenciales", "Día": "LUNES", "Hora Inicio": time(8,0), "Hora Fin": time(9,0)},
    {"Materia": "Ecuaciones Diferenciales", "Día": "MIERCOLES", "Hora Inicio": time(8,0), "Hora Fin": time(9,0)},
    {"Materia": "Ecuaciones Diferenciales", "Día": "JUEVES", "Hora Inicio": time(8,0), "Hora Fin": time(9,0)},
    {"Materia": "Ecuaciones Diferenciales", "Día": "VIERNES", "Hora Inicio": time(8,0), "Hora Fin": time(9,0)},
    {"Materia": "Ecuaciones Diferenciales", "Día": "MARTES", "Hora Inicio": time(9,0), "Hora Fin": time(10,0)},
    {"Materia": "Ecuaciones Diferenciales", "Día": "MARTES", "Hora Inicio": time(10,0), "Hora Fin": time(11,0)},
    {"Materia": "Ecuaciones Diferenciales", "Día": "LUNES", "Hora Inicio": time(11,0), "Hora Fin": time(12,0)},
    {"Materia": "Ecuaciones Diferenciales", "Día": "MARTES", "Hora Inicio": time(11,0), "Hora Fin": time(12,0)},
    {"Materia": "Ecuaciones Diferenciales", "Día": "MIERCOLES", "Hora Inicio": time(11,0), "Hora Fin": time(12,0)},
    {"Materia": "Ecuaciones Diferenciales", "Día": "JUEVES", "Hora Inicio": time(11,0), "Hora Fin": time(12,0)},
    {"Materia": "Ecuaciones Diferenciales", "Día": "LUNES", "Hora Inicio": time(12,0), "Hora Fin": time(13,0)},
    {"Materia": "Ecuaciones Diferenciales", "Día": "MARTES", "Hora Inicio": time(12,0), "Hora Fin": time(13,0)},
    {"Materia": "Ecuaciones Diferenciales", "Día": "MIERCOLES", "Hora Inicio": time(12,0), "Hora Fin": time(13,0)},
    {"Materia": "Ecuaciones Diferenciales", "Día": "JUEVES", "Hora Inicio": time(12,0), "Hora Fin": time(13,0)},
    {"Materia": "Ecuaciones Diferenciales", "Día": "LUNES", "Hora Inicio": time(14,0), "Hora Fin": time(15,0)},
    {"Materia": "Ecuaciones Diferenciales", "Día": "MARTES", "Hora Inicio": time(14,0), "Hora Fin": time(15,0)},
    {"Materia": "Ecuaciones Diferenciales", "Día": "MIERCOLES", "Hora Inicio": time(14,0), "Hora Fin": time(15,0)},
    {"Materia": "Ecuaciones Diferenciales", "Día": "JUEVES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0)},
    {"Materia": "Ecuaciones Diferenciales", "Día": "JUEVES", "Hora Inicio": time(16,0), "Hora Fin": time(17,0)},
    
    # Fundamentos de Matemáticas
    {"Materia": "Fundamentos de Matemáticas", "Día": "LUNES", "Hora Inicio": time(14,0), "Hora Fin": time(15,0)},
    {"Materia": "Fundamentos de Matemáticas", "Día": "MARTES", "Hora Inicio": time(14,0), "Hora Fin": time(15,0)},
    {"Materia": "Fundamentos de Matemáticas", "Día": "MIERCOLES", "Hora Inicio": time(14,0), "Hora Fin": time(15,0)},
    {"Materia": "Fundamentos de Matemáticas", "Día": "JUEVES", "Hora Inicio": time(14,0), "Hora Fin": time(15,0)},
    {"Materia": "Fundamentos de Matemáticas", "Día": "VIERNES", "Hora Inicio": time(14,0), "Hora Fin": time(15,0)},
    {"Materia": "Fundamentos de Matemáticas", "Día": "LUNES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0)},
    {"Materia": "Fundamentos de Matemáticas", "Día": "MARTES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0)},
    {"Materia": "Fundamentos de Matemáticas", "Día": "MIERCOLES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0)},
    {"Materia": "Fundamentos de Matemáticas", "Día": "JUEVES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0)},
    {"Materia": "Fundamentos de Matemáticas", "Día": "VIERNES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0)},
    
    # Sistemas Numéricos
    {"Materia": "Sistemas Numéricos", "Día": "MIERCOLES", "Hora Inicio": time(7,0), "Hora Fin": time(8,0)},
    {"Materia": "Sistemas Numéricos", "Día": "MIERCOLES", "Hora Inicio": time(8,0), "Hora Fin": time(9,0)},
    {"Materia": "Sistemas Numéricos", "Día": "VIERNES", "Hora Inicio": time(7,0), "Hora Fin": time(8,0)},
    {"Materia": "Sistemas Numéricos", "Día": "VIERNES", "Hora Inicio": time(8,0), "Hora Fin": time(9,0)},
    {"Materia": "Sistemas Numéricos", "Día": "LUNES", "Hora Inicio": time(9,0), "Hora Fin": time(10,0)},
    {"Materia": "Sistemas Numéricos", "Día": "LUNES", "Hora Inicio": time(10,0), "Hora Fin": time(11,0)},
    {"Materia": "Sistemas Numéricos", "Día": "LUNES", "Hora Inicio": time(11,0), "Hora Fin": time(12,0)},
    {"Materia": "Sistemas Numéricos", "Día": "MARTES", "Hora Inicio": time(11,0), "Hora Fin": time(12,0)},
    {"Materia": "Sistemas Numéricos", "Día": "JUEVES", "Hora Inicio": time(11,0), "Hora Fin": time(12,0)},
    {"Materia": "Sistemas Numéricos", "Día": "LUNES", "Hora Inicio": time(12,0), "Hora Fin": time(13,0)},
    {"Materia": "Sistemas Numéricos", "Día": "MARTES", "Hora Inicio": time(12,0), "Hora Fin": time(13,0)},
    {"Materia": "Sistemas Numéricos", "Día": "JUEVES", "Hora Inicio": time(12,0), "Hora Fin": time(13,0)},
    {"Materia": "Sistemas Numéricos", "Día": "MIERCOLES", "Hora Inicio": time(14,0), "Hora Fin": time(15,0)},
    {"Materia": "Sistemas Numéricos", "Día": "MIERCOLES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0)},
    {"Materia": "Sistemas Numéricos", "Día": "VIERNES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0)},
    {"Materia": "Sistemas Numéricos", "Día": "VIERNES", "Hora Inicio": time(16,0), "Hora Fin": time(17,0)},
]

# Función para filtrar monitorías
monitorias = [m for m in monitorias if m["Hora Fin"] <= time(19,0)]

# Convertir a DataFrame
df = pd.DataFrame(monitorias)

# Orden correcto de días
orden_dias = ["LUNES", "MARTES", "MIERCOLES", "JUEVES", "VIERNES"]
df["Día"] = pd.Categorical(df["Día"], categories=orden_dias, ordered=True)
df = df.sort_values(["Día", "Hora Inicio"])

# Función para formatear horas en AM/PM
def formato_hora(hora):
    if hora.hour < 12:
        return f"{hora.hour}:{hora.minute:02d} AM"
    elif hora.hour == 12:
        return f"12:{hora.minute:02d} PM"
    else:
        return f"{hora.hour-12}:{hora.minute:02d} PM"

# Función para filtrar monitorías
def filtrar_monitorias(materia_seleccionada, dia_seleccionado, hora_seleccionada):
    filtro = df.copy()
    
    if materia_seleccionada != "Todas":
        filtro = filtro[filtro["Materia"] == materia_seleccionada]
    
    if dia_seleccionado != "Todos":
        filtro = filtro[filtro["Día"] == dia_seleccionado]
    
    if hora_seleccionada:
        hora_seleccionada = time(hora_seleccionada.hour, hora_seleccionada.minute)
        filtro = filtro[
            (filtro["Hora Inicio"] <= hora_seleccionada) & 
            (hora_seleccionada < filtro["Hora Fin"])
        ]
    
    return filtro

# Interfaz de usuario
st.title("Monitorías del Departamento de Matemáticas UNAL")
st.subheader("Consulta disponibilidad de tutorías")

# Obtener opciones únicas
materias = ["Todas"] + sorted(df["Materia"].unique().tolist())
dias = ["Todos"] + orden_dias

# Widgets de selección
col1, col2 = st.columns(2)
with col1:
    materia_seleccionada = st.selectbox("Selecciona la materia:", materias)
with col2:
    dia_seleccionado = st.selectbox("Selecciona el día:", dias)

hora_libre = st.time_input("¿A qué hora estás libre?", 
                          value=None,
                          step=1800)  # Saltos de 30 minutos

# Botón de búsqueda
if st.button("Buscar Monitorías"):
    resultados = filtrar_monitorias(
        materia_seleccionada,
        dia_seleccionado,
        hora_libre
    )
    
    if resultados.empty:
        st.info("No se encontraron monitorías disponibles con esos criterios")
    else:
        st.success(f"📅 {len(resultados)} monitorías encontradas:")
        
        # Formatear resultados
        resultados_display = resultados.copy()
        resultados_display["Horario"] = resultados.apply(
            lambda x: f"{formato_hora(x['Hora Inicio'])} - {formato_hora(x['Hora Fin'])}", 
            axis=1
        )
        
        # Mostrar tabla ordenada
        st.dataframe(
            resultados_display[["Materia", "Día", "Horario"]],
            hide_index=True,
            column_config={
                "Materia": st.column_config.Column(width="medium"),
                "Día": st.column_config.Column(width="small"),
                "Horario": st.column_config.Column(width="medium")
            }
        )


# Información adicional
st.divider()
st.markdown("""
**Información importante:**
- Todas las monitorías se realizan en el **Salón 405-317** (excepto indicación especial)
- Horario de atención: **Lunes a Viernes de 7:00 am a 6:00 pm**
- En días festivos aplica horario especial (consultar en el departamento)
- Los horarios están sujetos a cambios durante el semestre
""")
