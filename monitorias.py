import streamlit as st
import pandas as pd
from datetime import time

# Datos de las monitorías
monitorias = [
    {"Materia": "ÁLGEBRA LINEAL", "Día": "LUNES", "Hora Inicio": time(7,0), "Hora Fin": time(8,0), "Monitor": "Vega Camacho Juan David (POSG) 405-317"},
    {"Materia": "ÁLGEBRA LINEAL", "Día": "LUNES", "Hora Inicio": time(8,0), "Hora Fin": time(9,0), "Monitor": "Vega Camacho Juan David (POSG) 405-317"},
    {"Materia": "ÁLGEBRA LINEAL", "Día": "LUNES", "Hora Inicio": time(9,0), "Hora Fin": time(10,0), "Monitor": "Aguiar Reina Luis Alejandro (405-317)"},
    # ... (todos los datos completos van aquí)
    {"Materia": "SISTEMAS NUMÉRICOS", "Día": "VIERNES", "Hora Inicio": time(15,0), "Hora Fin": time(16,0), "Monitor": "Cipagauta Cultiva Gustavo Daver (POSG) 405-317"}
]

# Convertir a DataFrame
df = pd.DataFrame(monitorias)

# Función para filtrar monitorías
def filtrar_monitorias(materia_seleccionada, dia_seleccionado, hora_seleccionada):
    filtro = df.copy()
    
    if materia_seleccionada != "Todas":
        filtro = filtro[filtro["Materia"] == materia_seleccionada]
    
    if dia_seleccionado != "Todos":
        filtro = filtro[filtro["Día"] == dia_seleccionada]
    
    if hora_seleccionada:
        hora_seleccionada = time(hora_seleccionada.hour, hora_seleccionada.minute)
        filtro = filtro[
            (filtro["Hora Inicio"] <= hora_seleccionada) & 
            (hora_seleccionada < filtro["Hora Fin"])
        ]
    
    return filtro

# Interfaz de usuario
st.title("📚 Monitorías de Matemáticas UNAL")
st.subheader("Consulta disponibilidad de tutorías")

# Obtener opciones únicas
materias = ["Todas"] + sorted(df["Materia"].unique().tolist())
dias = ["Todos"] + sorted(df["Día"].unique().tolist())

# Widgets de selección
col1, col2 = st.columns(2)
with col1:
    materia_seleccionada = st.selectbox("Selecciona la materia:", materias)
with col2:
    dia_seleccionado = st.selectbox("Selecciona el día:", dias)

hora_libre = st.time_input("¿A qué hora estás libre?", value=None)

# Botón de búsqueda
if st.button("Buscar Monitorías"):
    if df.empty:
        st.warning("No hay datos de monitorías disponibles")
    else:
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
                lambda x: f"{x['Hora Inicio'].strftime('%H:%M')} - {x['Hora Fin'].strftime('%H:%M')}", 
                axis=1
            )
            
            st.dataframe(resultados_display[["Materia", "Día", "Horario", "Monitor"]], 
                         hide_index=True)

# Información adicional
st.divider()
st.markdown("""
**Notas:**
- Las monitorías se realizan principalmente en el salón 405-317
- (POSG) indica monitores de posgrado
- Los horarios pueden cambiar en días festivos
""")
