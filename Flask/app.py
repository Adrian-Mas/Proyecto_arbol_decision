from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Cargar el modelo entrenado
with open("decision_tree_clasiffier_diabetes", "rb") as f:
    model = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        # Ejemplo: Recoger datos del formulario
        # Aquí se supone que tienes un formulario en el template que envía estos datos.
        try:
            # Se recogen los datos y se convierten a float
            pregnancies = float(request.form["Pregnancies"])
            glucose = float(request.form["Glucose"])
            blood_pressure = float(request.form["BloodPressure"])
            insulin = float(request.form["Insulin"])
            bmi = float(request.form["BMI"])
            dpf = float(request.form["DiabetesPedigreeFunction"])
            age = float(request.form["Age"])

            # Crear un DataFrame con los datos de entrada (como un solo registro)
            input_data = pd.DataFrame({
                "Pregnancies": [pregnancies],
                "Glucose": [glucose],
                "BloodPressure": [blood_pressure],
                "Insulin": [insulin],
                "BMI": [bmi],
                "DiabetesPedigreeFunction": [dpf],
                "Age": [age]
            })

            # Realizar la predicción
            prediction = model.predict(input_data)[0]
            result = "Positivo" if prediction == 1 else "Negativo"
        except Exception as e:
            result = f"Error en los datos: {e}"
    
    # En la vista, mostramos el resultado (si existe) y la vista previa del DataFrame, etc.
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)




