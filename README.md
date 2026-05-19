# Gerçek Zamanlı Yüz Bulanıklaştırma Uygulaması

## 📋 Proje Açıklaması

Bu proje, bilgisayarınıza bağlı bir kamera aracılığıyla alınan canlı görüntü üzerinde gerçek zamanlı olarak yüz tespiti yapan ve tespit edilen yüzleri otomatik olarak bulanıklaştıran bir uygulamadır. Bu sayede kişilerin gizliliği korunurken, gerçek zamanlı görüntü işleme teknikleri öğrenilebilir.

---

## 🎯 Projenin Amacı

- Canlı kamera görüntüsü üzerinde gerçek zamanlı yüz tespiti yapmak
- Tespit edilen yüz bölgelerine bulanıklaştırma efekti uygulamak
- Python ve OpenCV kütüphanesi ile görüntü işleme becerilerini geliştirmek
- Gerçek zamanlı uygulama geliştirme mantığını kavramak

---

## 🛠️ Kullanılan Teknolojiler ve Teknikler

| Teknoloji | Açıklama |
|-----------|----------|
| **Python 3.x** | Projenin temel programlama dili |
| **OpenCV (cv2)** | Görüntü işleme, kamera yönetimi ve yüz tanıma işlemleri |
| **Haar Cascade Classifier** | OpenCV'nin önceden eğitilmiş yüz tanıma modeli |
| **Gaussian Blur** | Tespit edilen yüz bölgesine bulanıklık efekti uygulama |

---

## ⚙️ Nasıl Çalışır?

1. Uygulama başlatıldığında bilgisayarınızdaki varsayılan kamera aktif hale gelir
2. Kameradan alınan her bir kare aynadaki görüntü gibi yatay olarak çevrilir
3. Kare, yüz tespiti için gri tonlamaya dönüştürülür
4. Haar Cascade algoritması ile kare içerisindeki yüzler tespit edilir
5. Tespit edilen her bir yüz bölgesine Gaussian bulanıklık uygulanır
6. Bulanıklaştırılmış görüntü canlı olarak bir pencerede gösterilir
7. Kullanıcı 'k' tuşuna basarak uygulamayı sonlandırabilir

---

## 📊 Akış Diyagramı
[Kameraları Başlat]
↓
[Kare Yakala] ←─────────┐
↓ │
[Yatay Çevirme] │
↓ │
[Gri Tonlamaya Çevir] │
↓ │
[Yüz Tespiti Yap] │
↓ │
[Yüzleri Bulanıklaştır] │
↓ │
[Görüntüyü Göster] │
↓ │
['k' tuşuna basıldı mı?]─┘
↓
[Kaynakları Serbest Bırak ve Çıkış]

---

## 📦 Gerekli Kütüphaneler ve Kurulum

Projeyi çalıştırmak için öncelikle gerekli kütüphaneleri yüklemeniz gerekmektedir:

terminale 'pip install opencv-contrib-python'kodunu yapıştırın.

---
🔧 Kod Açıklamaları
Kod Bloğu	Açıklama
cv2.VideoCapture(0)	Varsayılan kamerayı başlatır
cv2.flip(kare, 1)	Görüntüyü yatay olarak çevirir (ayna efekti)
cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)	Renkli görüntüyü gri tonlamaya çevirir
detectMultiScale()	Haar Cascade ile görüntüdeki yüzleri tespit eder
cv2.GaussianBlur()	Belirtilen bölgeye Gaussian bulanıklık uygular
cv2.imshow()	İşlenmiş görüntüyü pencerede gösterir
cv2.waitKey(1)	Klavye girişini kontrol eder

---
⚠️ Olası Sorunlar ve Çözümleri
Sorun	Olası Çözüm
Kamera açılmıyor	Kameranın başka bir uygulama tarafından kullanılmadığından emin olun
"ModuleNotFoundError: No module named 'cv2'"	pip install opencv-python komutunu çalıştırın
Yüzler tespit edilmiyor	Işıklandırmayı iyileştirin veya minNeighbors değerini düşürün
Uygulama yavaş çalışıyor	Bulanıklaştırma çekirdek boyutunu küçültün (ör: 151 yerine 51)
📈 Performans İyileştirme Önerileri
Daha hızlı çalışma için: minSize parametresini artırın (örn: minSize=(80, 80))

Daha iyi yüz tespiti için: scaleFactor parametresini 1.05 gibi daha düşük bir değere ayarlayın

Daha hafif bulanıklık için: Gaussian blur çekirdek boyutunu (51, 51) gibi küçültün

---

📝 Ek Notlar
Haar Cascade modeli, OpenCV'nin kendi içinde gömülü olarak gelir ve harici olarak indirilmesine gerek yoktur

Pygame kütüphanesi bu kodda kullanılmamıştır, gereksiz import yapılmıştır (isteğe bağlı kaldırılabilir)

Uygulama çalışırken kamera ışığının yanacağını unutmayın

---

👨‍💻 Geliştirici
Samet Erdoğan
Acunmedya Akademi Bitirme Projesi
