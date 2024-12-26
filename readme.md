
# ESP8266 ve ESP32 Soket Haberleşmesi Projesi

## Proje Tanımı
Bu proje, ESP8266 ve ESP32 mikrodenetleyicileri arasında soket haberleşmesi ile veri iletimini gerçekleştirmektedir. Projede, ESP8266 üzerinde bağlı bulunan HCSR04 mesafe sensörü ve LDR ışık sensörü verileri AES veya Sezar şifreleme yöntemleri ile şifrelenip, UDP paketi olarak ESP32'ye gönderilmektedir. ESP32 üzerinde yürütülen UDP sunucu soketi, gelen paketleri yakalamakta, şifresini çözmekte ve belirli aksiyonlar almaktadır. ESP32 üzerinde bir adet OLED ekran ve bir adet harici LED bulunmaktadır. ESP8266'dan gelen verilerin çözümlenmiş hali bu ekranda görüntülenmektedir. Gelen veride ortamda ışık yok '0' verisi varsa, ESP32 üzerindeki LED aktif hale gelmektedir, aksi halde kapalı halde bulunur.

## Proje Yapısı
| **Dosya**                                    | **Açıklama**                                                                                       |
|----------------------------------------------|---------------------------------------------------------------------------------------------------|
| **boot.py**                                  | - Projenin başlangıç dosyasıdır.                                                                 |
|                                              | - ESP32 veya ESP8266 için gerekli bağlantı ayarlarını yapar ve ana fonksiyonu çalıştırır.        |
| **home/main_32.py**                          | - ESP32 üzerinde çalışacak olan ana fonksiyonları içerir.                                        |
|                                              | - UDP sunucusunu başlatır ve gelen verileri OLED ekranda görüntüler.                             |
| **home/main_82.py**                          | - ESP8266 üzerinde çalışacak olan ana fonksiyonları içerir.                                      |
|                                              | - Sensör verilerini okur, şifreler ve UDP paketi olarak gönderir.                                |
| **home/connection/udp_server.py**            | - UDP sunucusunu başlatır ve gelen verileri işler.                                               |
|                                              | - Gelen verileri çözerek OLED ekranda görüntüler ve LED'i kontrol eder.                         |
| **home/connection/connection.py**            | - ESP8266 ve ESP32'nin WiFi bağlantılarını yönetir.                                              |
| **home/connection/socket_send.py**           | - UDP ve TCP soket bağlantılarını yönetir.                                                       |
| **home/methods/aes.py**                      | - AES şifreleme işlemlerini gerçekleştirir.                                                      |
| **home/communication/messages/message_manipulator.py** | - Mesajları şifreler ve çözer.                                                  |
| **home/hardware/hcsr04.py**                  | - HCSR04 mesafe sensörünü kontrol eder ve veri okur.                                             |
| **home/hardware/ldr.py**                     | - LDR ışık sensörünü kontrol eder ve veri okur.                                                  |
| **home/hardware/display.py**                 | - OLED ekranı kontrol eder ve veri görüntüler.                                                   |
| **home/hardware/led.py**                     | - Harici LED'i kontrol eder.                                                                     |


## Kurulum ve Kullanım

1. **Bağlantı Ayarları:**
   - `boot.py` dosyasındaki IP, alt ağ maskesi, ağ geçidi ve DNS bilgilerini kendi ağınıza göre ayarlayın.

2. **ESP8266 ve ESP32'yi Programlayın:**
   - `home/main_82.py` dosyasını ESP8266'ya yükleyin.
   - `home/main_32.py` dosyasını ESP32'ye yükleyin.

3. **Çalıştırma:**
   - Her iki cihazı da çalıştırın.
   - ESP8266 sensör verilerini okuyacak, şifreleyecek ve UDP paketi olarak ESP32'ye gönderecektir.
   - ESP32 gelen verileri çözecek, OLED ekranda görüntüleyecek ve LED'i kontrol edecektir.
