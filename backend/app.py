from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle
import os  # EKLENDİ

app = Flask(__name__)
CORS(app)

# ✅ model.pkl'e doğru yoldan eriş
file_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(file_path, "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return "Backend çalışıyor!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        input_data = {
            "Net Metrekare": float(data["metrekare"]),
            "Oda Sayısı": int(data["oda_sayisi"]),
            "Binanın Yaşı": int(data["bina_yasi"]),
            "İlçe": data["ilce"]
        }

        input_df = pd.DataFrame([input_data])
        input_df = pd.get_dummies(input_df)

        for col in model.feature_names_in_:
            if col not in input_df.columns:
                input_df[col] = 0

        input_df = input_df[model.feature_names_in_]

        prediction = model.predict(input_df)[0]

        # Türk lirası formatında göster
        formatted_price = f"{prediction:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        return jsonify({"predicted_price": formatted_price})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/favicon.ico")
def favicon():
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)
