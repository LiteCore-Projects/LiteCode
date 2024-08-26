# LiteCode Programlama Dili Fonksiyonları

## Temel Fonksiyonlar

### `print`, `echo`, `write`
- **Açıklama:** Terminale metin yazdırır.
- **Sözdizimi:** `print <metin>`
- **Örnek:** `print Merhaba Dünya!`
- **Renk Kullanımı:** `print <kırmızı mavi>Kırmızı metin, mavi arka plan`

### `insert`
- **Açıklama:** Belirli bir terminal koordinatına metin ekler.
- **Sözdizimi:** `insert <x> <y> <metin>`
- **Örnek:** `insert 10 5 Merhaba`
- **Renk Kullanımı:** `insert 10 5 <yeşil>Yeşil metin`

### `run`
- **Açıklama:** Başka bir LiteCode betiğini çalıştırır.
- **Sözdizimi:** `run <dosya_ismi>`
- **Örnek:** `run script.lc`

### `wait`
- **Açıklama:** Belirtilen saniye kadar bekler.
- **Sözdizimi:** `wait <saniye>`
- **Örnek:** `wait 5`

### `set`
- **Açıklama:** Bir değişkenin değerini ayarlar.
- **Sözdizimi:** `set <değişken>=<değer>`
- **Örnek:** `set myVar=10`

### `if`
- **Açıklama:** Koşullu kod yürütme.
- **Sözdizimi:** `if <koşul>`
- **Örnek:** `if $myVar == 10`

### `math`
- **Açıklama:** Matematiksel bir işlem yapar ve sonucu saklar.
- **Sözdizimi:** `math <ifade>`
- **Örnek:** `math $myVar + 5`

### `size`
- **Açıklama:** Terminal boyutunu ayarlar.
- **Sözdizimi:** `size <sütun> <satır>`
- **Örnek:** `size 80 24`

### `input`
- **Açıklama:** Kullanıcıdan girdi alır ve bir değişkende saklar.
- **Sözdizimi:** `input <istek_metin>`
- **Örnek:** `input Adınızı girin:`

### `split`
- **Açıklama:** Bir değişkeni boşluklarla ayırır ve parçaları sıralı değişkenlerde saklar.
- **Sözdizimi:** `split <değişken>`
- **Örnek:** `split $myVar`

### `clear`, `cls`
- **Açıklama:** Terminal ekranını temizler.
- **Sözdizimi:** `clear`

### `cd`
- **Açıklama:** Geçerli dizini değiştirir.
- **Sözdizimi:** `cd <hedef_klasör>`
- **Örnek:** `cd /yol/klasör`

### `loop`
- **Açıklama:** Betiğin döngüsel olarak çalışmasını etkinleştirir veya devre dışı bırakır.
- **Sözdizimi:** `loop <true|false>`
- **Örnek:** `loop true`

### `exit`
- **Açıklama:** Betikten çıkış yapar.
- **Sözdizimi:** `exit`

### `random`
- **Açıklama:** Belirli bir aralıkta rastgele bir sayı üretir ve bir değişkende saklar.
- **Sözdizimi:** `random <min> <max>`
- **Örnek:** `random 1 100`

### `delete`
- **Açıklama:** Belirtilen dosyayı siler.
- **Sözdizimi:** `delete <dosya_ismi>`
- **Örnek:** `delete temp.txt`

### `download`
- **Açıklama:** Bir URL'den dosya indirir.
- **Sözdizimi:** `download <url> <hedef_yol>`
- **Örnek:** `download http://example.com/dosya.txt dosya.txt`

### `read`
- **Açıklama:** Bir dosyanın belirli bir satırını okur.
- **Sözdizimi:** `read <dosya_ismi> <satır_numarası>`
- **Örnek:** `read myfile.txt 5`

### `edit`
- **Açıklama:** Bir dosyanın belirli bir satırını düzenler.
- **Sözdizimi:** `edit <dosya_ismi> <satır_numarası> <yeni_metin>`
- **Örnek:** `edit myfile.txt 3 Yeni içerik`

### `del`
- **Açıklama:** Bir dosyadan belirli bir satırı siler.
- **Sözdizimi:** `del <dosya_ismi> <satır_numarası>`
- **Örnek:** `del myfile.txt 2`

### `dir`
- **Açıklama:** Bir dizinin içeriğini listeler.
- **Sözdizimi:** `dir <dizin_yolu>`
- **Örnek:** `dir /yol/klasör`

### `send`
- **Açıklama:** Bir dosyayı bulut veritabanına gönderir.
- **Sözdizimi:** `send <dosya_ismi> <bulut_klasörü>`
- **Örnek:** `send myfile.txt bulut_klasör`

### `get`
- **Açıklama:** Bulut veritabanından veri alır ve bir dosyaya kaydeder.
- **Sözdizimi:** `get <dosya_ismi>`
- **Örnek:** `get myfile.txt`

### `list`
- **Açıklama:** Bulut veritabanından verileri listeler.
- **Sözdizimi:** `list`
