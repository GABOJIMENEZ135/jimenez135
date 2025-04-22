import streamlit as st

st.title("Calculadora de la Ecuación Combinada de los Gases Ideales")

st.markdown("""
Esta app resuelve la ecuación combinada de los gases ideales:

\\[
\\frac{P_1 V_1}{T_1} = \\frac{P_2 V_2}{T_2}
\\]

Donde:
- Presión (P) en **atm**
- Volumen (V) en **litros**
- Temperatura (T) en **kelvin**
""")

# Variables
variables = {
    "P1": "Presión 1 (atm)",
    "V1": "Volumen 1 (L)",
    "T1": "Temperatura 1 (K)",
    "P2": "Presión 2 (atm)",
    "V2": "Volumen 2 (L)",
    "T2": "Temperatura 2 (K)"
}

# Selección de variable a calcular
missing = st.selectbox("¿Qué variable deseas calcular?", list(variables.keys()))

# Inputs para las demás variables
inputs = {}
for var in variables:
    if var != missing:
        inputs[var] = st.number_input(f"Ingrese {variables[var]}:", min_value=0.0001)

# Botón de cálculo
if st.button("Calcular"):
    try:
        P1 = inputs.get("P1", None)
        V1 = inputs.get("V1", None)
        T1 = inputs.get("T1", None)
        P2 = inputs.get("P2", None)
        V2 = inputs.get("V2", None)
        T2 = inputs.get("T2", None)

        if missing == "P1":
            result = (P2 * V2 * T1) / (V1 * T2)
        elif missing == "V1":
            result = (P2 * V2 * T1) / (P1 * T2)
        elif missing == "T1":
            result = (P1 * V1 * T2) / (P2 * V2)
        elif missing == "P2":
            result = (P1 * V1 * T2) / (V2 * T1)
        elif missing == "V2":
            result = (P1 * V1 * T2) / (P2 * T1)
        elif missing == "T2":
            result = (P2 * V2 * T1) / (P1 * V1)
        else:
            result = None

        st.success(f"{variables[missing]} = {result:.4f}")
    except Exception as e:
        st.error(f"Error en el cálculo: {e}")
