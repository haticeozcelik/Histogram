# Gerekli kütüphaneler ekleniyor.
from PIL import Image  # Görüntü işleme için PIL kütüphanesi
import matplotlib.pyplot as plt  # Grafik çizimi için matplotlib kütüphanesi

# Renk bileşenlerini elde etmek için fonksiyonlar tanımlanıyor.
def getRed(redVal):
    return '#%02x%02x%02x' % (redVal, 0, 0)  # Kırmızı bileşenini oluşturan hexadecimal renk kodu

def getGreen(greenVal):
    return '#%02x%02x%02x' % (0, greenVal, 0)  # Yeşil bileşenini oluşturan hexadecimal renk kodu

def getBlue(blueVal):
    return '#%02x%02x%02x' % (0, 0, blueVal)  # Mavi bileşenini oluşturan hexadecimal renk kodu

# Resim dosyası açılıyor.
image = Image.open("./tavus.jpg")  # 'tavus.jpg' adlı resim dosyası açılıyor

# Belirli piksellere yeni renk değerleri atanıyor.
image.putpixel((0, 1), (1, 1, 5))  # (0, 1) konumundaki piksele yeni bir renk değeri atanıyor
image.putpixel((0, 2), (2, 1, 5))  # (0, 2) konumundaki piksele yeni bir renk değeri atanıyor

# Resim gösteriliyor.
image.show()  # Değiştirilmiş resim gösteriliyor

# Resmin histogramı hesaplanıyor.
histogram = image.histogram()  # Resmin histogramı hesaplanıyor

# Histogramın R, G, B bileşenleri için ayrılması.
l1 = histogram[0:256]    # Kırmızı (Red) bileşeninin histogramı
l2 = histogram[256:512]  # Yeşil (Green) bileşeninin histogramı
l3 = histogram[512:768]  # Mavi (Blue) bileşeninin histogramı

# R bileşeni histogramının grafiği çiziliyor.
plt.figure(0)  # Yeni bir grafik figürü oluşturuluyor
for i in range(0, 256):
    plt.bar(i, l1[i], color=getRed(i), edgecolor=getRed(i), alpha=0.3)  # Her bir kırmızı bileşeninin histogram çubuğu çiziliyor

# G bileşeni histogramının grafiği çiziliyor.
plt.figure(1)  # Yeni bir grafik figürü oluşturuluyor
for i in range(0, 256):
    plt.bar(i, l2[i], color=getGreen(i), edgecolor=getGreen(i), alpha=0.3)  # Her bir yeşil bileşeninin histogram çubuğu çiziliyor

# B bileşeni histogramının grafiği çiziliyor.
plt.figure(2)  # Yeni bir grafik figürü oluşturuluyor
for i in range(0, 256):
    plt.bar(i, l3[i], color=getBlue(i), edgecolor=getBlue(i), alpha=0.3)  # Her bir mavi bileşeninin histogram çubuğu çiziliyor

# Grafiği göster.
plt.show()  # Oluşturulan histogramları göster
