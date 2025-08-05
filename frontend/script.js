document.getElementById("predictForm").addEventListener("submit", function(e) {
  e.preventDefault();

  const formData = new FormData(e.target);
  const data = Object.fromEntries(formData.entries());

  if (data.metrekare > 300 || data.oda_sayisi > 10 || data.bina_yasi > 150) {
    alert("Lütfen geçerli değerler giriniz.");
    return;
  }

  document.getElementById("result").innerText = "Tahmin yapılıyor...";

  fetch("http://localhost:5000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  })
  .then(res => res.json())
  .then(result => {
    if (result.predicted_price !== undefined) {
      document.getElementById("result").innerText = `Tahmini Fiyat: ${result.predicted_price} TL`;
    } else {
      document.getElementById("result").innerText = `Hata: ${result.error}`;
    }
  });
});
