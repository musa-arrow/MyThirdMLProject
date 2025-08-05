import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Veri setini oku
df = pd.read_csv("data.csv", delimiter=";")

# Gerekli sütunları seç
df = df[["Net Metrekare", "Oda Sayısı", "Binanın Yaşı", "Fiyat", "İlçe"]]

# Metrekare
df["Net Metrekare"] = df["Net Metrekare"].str.replace(" m²", "").str.replace(",", ".").astype(float)

# Oda sayısı (örneğin 2+1 → 3)
df["Oda Sayısı"] = df["Oda Sayısı"].apply(lambda x: sum([float(i) for i in x.split("+")]) if "+" in x else None)

# Bina yaşı
def convert_age(age):
    if age == "0 (Yeni)":
        return 0
    elif age == "21 Ve Üzeri":
        return 21
    elif "-" in age:
        return int(age.split("-")[0])
    else:
        return None

df["Binanın Yaşı"] = df["Binanın Yaşı"].apply(convert_age)

# Fiyat
df["Fiyat"] = df["Fiyat"].str.replace(".", "").str.replace(",", ".").astype(float)

# Eksik verileri ve aykırı fiyatları temizle
df = df.dropna()
df = df[df["Fiyat"] < 10_000_000]

# Özellik ve hedef
X = df[["Net Metrekare", "Oda Sayısı", "Binanın Yaşı", "İlçe"]]
y = df["Fiyat"]

# İlçeyi sayısala çevir
X = pd.get_dummies(X)

# Model eğitimi
model = RandomForestRegressor(n_estimators=200, max_depth=20, random_state=42)
model.fit(X, y)

# Modeli kaydet
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model başarıyla eğitildi ve kaydedildi.")
