# LiteCode Kurulumu

LiteCode'u kullanmaya başlamadan önce, aşağıdaki adımları izleyerek kurulumu gerçekleştirebilirsiniz.

## Windows İçin Kurulum

1. **İndirme ve Başlatma**: [LiteCode Installer](https://github.com/LiteCore-Projects/LiteCode/raw/main/LiteCode%20Installer.exe) dosyasını indirin.
2. **Yönetici Olarak Çalıştırma**: İndirdiğiniz Installer dosyasını **yönetici olarak başlatın**. Bu, programın gerekli izinlere sahip olmasını sağlar ve kurulumun sorunsuz tamamlanmasını sağlar.

## Linux İçin Kurulum

1. **Gerekli Kütüphaneleri Yükleme**: LiteCode'un çalışması için gerekli bazı kütüphaneleri manuel olarak kurmanız gerekmektedir. Aşağıdaki komutu kullanarak gerekli kütüphaneleri yükleyebilirsiniz:

   ```python
   pip install blessed
   pip install glob
   #hata veren diğer kütüphaneler
   ```
   bunları kurmak yeterli olacaktır eğer kütüphane bulunamadı hatası alırsanız hata verdiği kütüphaneyi pip install yöntemi ile kurun.
2. **Kaynak Koddan Çalıştırma:** LiteCode'u doğrudan kaynak koddan çalıştırmak için [litecode.py](https://github.com/LiteCore-Projects/LiteCode/raw/main/source/litecode.py) dosyasını kullanabilirsiniz. Bir LiteCode dosyasını çalıştırmak için aşağıdaki komutu kullanın:
   ```python
   python litecode.py <litecode dosyası>
   ```
   Bu adımları izleyerek LiteCode'u sorunsuz bir şekilde kurabilir ve kullanmaya başlayabilirsiniz.
