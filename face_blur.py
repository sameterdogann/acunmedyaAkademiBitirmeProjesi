#Eklediğim Kütüphaneler
import cv2
import pygame

#pygame i çalıştır
pygame.init()

# Seçili Kamerayı aç 
kamera = cv2.VideoCapture(0)

# Haar Cascade modelini yükle
cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
yuz_cascade = cv2.CascadeClassifier(cascade_path)

while True:
    ret, kare = kamera.read()
    if not ret:
        # Kameradan görüntü alamazsak döngüden çık
        break

    # Kameradaki görüntü ters ise düzeltmek için yataya çeviriyoruz
    kare = cv2.flip(kare, 1)

    # Griye çevir (yüz tespiti için)
    gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
    yuzler = yuz_cascade.detectMultiScale(gri, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))

    for (x, y, w, h) in yuzler:
        # Yüz bölgesini alıyoruz
        yüz_bölgesi = kare[y:y+h, x:x+w]

        # Tespit edilen yüzü bulanıklaştırır
        bulanık_yüz = cv2.GaussianBlur(yüz_bölgesi, (151, 151), 80)

  # Sadece yüz bölgesini tamamen bulanıklaştırıyoruz
        kare[y:y+h, x:x+w] = bulanık_yüz
   
 # Sonucu gösteriyoruz
    cv2.imshow('Gerçek Zamanlı Yüz Bulanıklaştırma', kare)

    # Pencereyi kapatmak için 'k' tuşuna basın veya pencereyi kapatın
    tuş = cv2.waitKey(1)
    if tuş & 0xFF == ord('k') or cv2.getWindowProperty('Gerçek Zamanlı Yüz Bulanıklaştırma', cv2.WND_PROP_VISIBLE) < 1:
        break

# Kamerayı kapatma
kamera.release()
# Tüm pencereleri kapat
cv2.destroyAllWindows()
