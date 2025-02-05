import streamlit as st
import pandas as pd
import pickle

# Cargar el modelo entrenado (asegúrate de que el archivo esté en la misma carpeta)
with open("decision_tree_clasiffier_diabetes", "rb") as f:
    model = pickle.load(f)

# Título de la aplicación
st.title("Prediciendo la Diabetes")

st.write("Introduce los siguientes datos:")

# Usaremos un formulario para organizar los inputs
with st.form(key="prediction_form"):
    pregnancies = st.number_input("Pregnancies", min_value=0, value=0)
    glucose = st.number_input("Glucose", min_value=0, value=0)
    blood_pressure = st.number_input("BloodPressure", min_value=0, value=0)
    insulin = st.number_input("Insulin", min_value=0, value=0)
    bmi = st.number_input("BMI", min_value=0.0, value=0.0, format="%.2f")
    dpf = st.number_input("DiabetesPedigreeFunction", min_value=0.0, value=0.0, format="%.2f")
    age = st.number_input("Age", min_value=0, value=0)
    
    # Botón para enviar el formulario
    submit_button = st.form_submit_button(label="Predecir")

# Si el usuario envía el formulario, se realiza la predicción
if submit_button:
    # Crear un DataFrame con los datos de entrada (una sola fila)
    input_data = pd.DataFrame({
        "Pregnancies": [pregnancies],
        "Glucose": [glucose],
        "BloodPressure": [blood_pressure],
        "Insulin": [insulin],
        "BMI": [bmi],
        "DiabetesPedigreeFunction": [dpf],
        "Age": [age]
    })
    
    try:
        # Realizar la predicción
        prediction = model.predict(input_data)[0]
        result = "Positivo" if prediction == 1 else "Negativo"
    except Exception as e:
        result = f"Error en los datos: {e}"
    
    # Mostrar el resultado en la interfaz de Streamlit
    st.write("Resultado de la predicción:", result)
