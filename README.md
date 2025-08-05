
# Ev Fiyat Tahmini - MyThirdMLProject

Bu proje, İstanbul'daki ev fiyatlarını tahmin etmek için geliştirilmiş bir makine öğrenmesi uygulamasıdır.  
Kullanıcıdan alınan metrekare, oda sayısı, bina yaşı ve ilçe bilgilerine göre ev fiyatı tahmini yapılmaktadır.

---

## İçindekiler

- [Proje Hakkında](#proje-hakkında)  
- [Kurulum](#kurulum)  
- [Kullanım](#kullanım)  
- [Model Eğitimi](#model-eğitimi)  
- [Frontend](#frontend)  
- [Model Performansı](#model-performansı)  
- [Katkıda Bulunma](#katkıda-bulunma)  
- [Lisans](#lisans)  

---

## Proje Hakkında

Bu projede, İstanbul'daki konut piyasasına ait veriler kullanılarak bir ev fiyat tahmin modeli geliştirilmiştir.  
Veri setindeki özellikler:  

- Net metrekare  
- Oda sayısı (örn. "2+1" → 3 oda)  
- Binanın yaşı  
- İlçe  

Makine öğrenmesi modeli olarak **Random Forest Regressor** kullanılmıştır. Model, veri temizliği ve ön işleme adımlarından sonra eğitilmiş ve pickle ile kaydedilmiştir.

---

## Kurulum

1. Depoyu klonlayın:

```bash
git clone https://github.com/musa-arrow/MyThirdMLProject.git
cd MyThirdMLProject
```

2. Sanal ortam oluşturup aktif edin (opsiyonel önerilir):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Gerekli paketleri yükleyin:

```bash
pip install -r requirements.txt
```

---

## Kullanım

### Model Eğitimi

Modeli yeniden eğitmek için:

```bash
python train_model.py
```

`train_model.py` dosyası:

- `data.csv` dosyasını okur, gerekli ön işlemleri yapar,  
- RandomForestRegressor ile modeli eğitir,  
- Modeli `model.pkl` olarak kaydeder.

### Backend (API)

Flask tabanlı backend'i çalıştırmak için:

```bash
python app.py
```

- API `/predict` endpoint'i POST ile JSON formatında `metrekare`, `oda_sayisi`, `bina_yasi` ve `ilce` bilgilerini alır,  
- Eğitilmiş modeli kullanarak tahmin yapar ve sonucu JSON olarak döner.

### Frontend

`index.html` dosyası kullanıcı arayüzünü sağlar.  

- İlçe, metrekare, oda sayısı ve bina yaşı bilgileri kullanıcıdan alınır,  
- Backend'e istek gönderilir ve tahmini fiyat kullanıcıya gösterilir.  
- Mobil uyumlu tasarım ve ek görseller/dokümanlar içerir.

---

## Model Performansı

- Model Doğruluk Oranı: %92.3  
- Ortalama Hata Payı: ±%7.7  
- R² Skoru: 0.89  

---

## Katkıda Bulunma

1. Repoyu forkla  
2. Yeni bir branch aç (`git checkout -b feature/yeni-ozellik`)  
3. Değişikliklerini commit et (`git commit -m 'Yeni özellik eklendi'`)  
4. Branch’e push yap (`git push origin feature/yeni-ozellik`)  
5. Pull request aç  

---

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır.

---

## İletişim

Musa Ok – musaok425@gmail.com  

---

