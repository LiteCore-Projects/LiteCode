# LiteCode Programlama Dili

LiteCode, Ömer Dilek tarafından geliştirilen bir programlama dilidir. Bu dil, basit ve etkili bir yazım biçimi sunarak kullanıcıların hızlı ve kolay bir şekilde program yazmalarını sağlar. LiteCode'un temel özellikleri ve fonksiyonları aşağıda özetlenmiştir.

## Özellikler

- **Basit Syntax**: LiteCode, öğrenilmesi ve kullanılması kolay bir sözdizimi sunar. Programcılar, kodlarını hızlıca yazabilir ve test edebilirler.
- **Renkli Çıktılar**: Terminal çıktılarında metin renklerini ve arka plan renklerini ayarlamak mümkündür.
- **Koordinat ile Yazı Yazma**: Terminalde belirli koordinatlara metin yazmak için destek sunar.
- **Dosya İşlemleri**: Dosya okuma, yazma, düzenleme ve silme gibi temel dosya işlemleri desteklenir.

## Fonksiyonlar

### `terminal_boyutlarini_al()`
- Terminalin genişlik ve yükseklik boyutlarını döndürür.

### `temp_dosyalari_sil()`
- Geçici (`temp_*.lc`) dosyalarını siler.

### `cd(target_folder)`
- Belirtilen klasöre geçiş yapar. Klasör mevcut değilse, bir hata mesajı verir.

### `handle_print_command(args)`
- Metin ve renk formatlarını işleyerek terminalde renkli metin çıktısı sağlar.

### `handle_insert_command(args)`
- Belirtilen koordinatlara metin yerleştirir ve renk formatlarını uygular.

### `argsdo()`
- Kod içindeki değişkenleri, `variables` sözlüğündeki değerlerle değiştirir.

### `terminal_boyutunu_ayarla(cols, lines)`
- Terminal boyutlarını ayarlar.

### `setrunner(filename)`
- Verilen dosyayı okur, yorumları ve boş satırları temizler ve geçici bir dosyaya yazar.

### `cumle_sozluk_olustur(cumle)`
- Virgüllerle ayrılmış bir cümleyi sözlüğe dönüştürür.

### `satir_sayisi(dosya_adi)`
- Belirtilen dosyanın satır sayısını döndürür.

### `calistir(dosya_yolu)`
- Belirtilen dosyayı bir terminalde çalıştırır.

### `read(anahtar_yolu)`
- Verilen anahtar yoluna göre veri okur.

### `oku(dosya_adi, satir_no)`
- Belirtilen dosyadaki belirli bir satırı okur.

### `printxy(x, y, yazi)`
- Terminalde belirtilen koordinatlara metin yazar.

### `klasor_olustur(yol)`
- Belirtilen yolda bir klasör oluşturur.

### `litecode.run(file)`
- LiteCode dosyasını çalıştırır. Dosya içindeki komutları analiz eder ve uygular.

## Kullanım Örneği

LiteCode komutları, basit bir sözdizimi ile yazılır ve çalıştırılır. Aşağıda bir örnek komut listesi verilmiştir:

```litecode
print "<red> Merhaba Dünya! <none>"
insert 10 5 "<green> Bu bir test mesajı <none>"
cd yeni_klasor
