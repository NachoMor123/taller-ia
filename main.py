import streamlit as st
from ia_diagnosticador import AsistenteMecanicoIA  # Importamos tu clase POO

# ==========================================
# CONFIGURACIÓN DE LA PÁGINA
# ==========================================
st.set_page_config(page_title="Scanner IA - Taller", page_icon="🚗")

# Poné tu API Key acá para probar rápido (¡no se la muestres a nadie!)
MI_LLAVE_API = "AIzaSyA_pW5woRsgAmHiVx8wM5iCDdoJXp7fCnk" 

# Inicializamos el motor de la IA
@st.cache_resource  # Esto hace que la IA se conecte una sola vez, no cada vez que tocas un botón
def inicializar_ia():
    return AsistenteMecanicoIA(api_key=MI_LLAVE_API)

try:
    motor_ia = inicializar_ia()
except Exception as e:
    st.error(f"Error al conectar con la IA. Revisá tu API Key. Detalle: {e}")
    st.stop()  # Detiene la app si no hay conexión

# ==========================================
# DISEÑO DE LA INTERFAZ
# ==========================================
st.title("🚗 Diagnosticador OBD2 con IA")
st.markdown("---")

with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        vehiculo = st.text_input("🚙 Vehículo y Motor", placeholder="Ej: VW Gol Trend 1.6")
    
    with col2:
        codigo_falla = st.text_input("🔍 Código OBD2", placeholder="Ej: P0300")

st.markdown("---")

# Botón grande para diagnosticar
if st.button("🚀 Iniciar Diagnóstico Inteligente", use_container_width=True):
    # Validamos que el mecánico haya puesto datos
    if not vehiculo or not codigo_falla:
        st.warning("⚠️ Por favor, completá ambos campos antes de continuar.")
    else:
        # Mostramos una animación de carga
        with st.spinner(f"Analizando {codigo_falla} para {vehiculo}... Esto puede tardar unos segundos."):
            
            # --- LLAMADA A TU CLASE POO ---
            # Llamamos al método que ya programaste en el otro archivo
            diagnostico_ia = motor_ia.diagnosticar_codigo(vehiculo, codigo_falla)
            # ------------------------------
            
            # Mostramos el resultado en una caja "joya"
            st.success("✅ Análisis completado")
            st.subheader(f"📋 Reporte para {vehiculo}")
            st.markdown("---")
            st.markdown(diagnostico_ia)  # Imprimimos lo que nos devolvió la IA

st.markdown("---")
st.caption("Herramienta de prueba. Siempre verificá físicamente en el vehículo.")