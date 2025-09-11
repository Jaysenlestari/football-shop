1. Data delivery adalah proses pengiriman suatu data dari sistem yang satu ke sistem lainnya. Proses ini diperlukan karena kita memerlukan komunikasi misalnya antar backend dengan frontend, menjamin datanya real time, lebih efisien dan akurat.
2. Menurut saya, json. Karena json memakai struktur key:value yang mudah dibaca. Selain itu ternyata hal itu membuat json lebih mudah diparsing terutama di javascript, membuatnya sangat cocok untuk API modern, aplikasi mobile, dan web services. Sebaliknya XML memakai struktur tree yang lebih susah dibaca dan kompleks, namun XML mendukung berbagai tipe data dan validasi dokumen yang lebih ketat. JSON lebih populer karena file lebih kecil, parsing lebih mudah, lebih aman dari beberapa serangan yang rentan pada XML, dan secara umum dirancang untuk mempermudah pertukaran data antar sistem. [source](https://aws.amazon.com/compare/the-difference-between-json-xml/) 
3. Method is_valid() digunakan untuk melakukan validasi input, method ini akan memeriksa apakah semua field di form terisi dengan data yang sesuai dengan format yang telah ditentukan (seperti length, tidak boleh kosong, dll). Sehingga dengan adanya method ini, akan ada validasi yang dilakukan terlebih dahulu terhadap data yang diisi user sebelum dikirim.
4. csrf_token adalah token unik yang dihasilkan oleh server dan disisipkan ke form. Saat form dikirim, Django akan melakukan validasi terhadap token tersebut. Hal ini mencegah penyerang membuat request palsu yang tampak seolah-olah berasal dari korbannya. Jika kita tidak menambahkan csrf_token, penyerang bisa membuat form berbahaya di website lain yang secara otomatis mengirim request ke server django ketika user (yang sedang login di web kita) mengunjungi situs penyerang (client-side). Karena browser otomatis mengirim cookie session, server akan menganggap request tersebut sah. Sehingga tentu saja hal ini berbahaya, karena attacker bisa mengganti password atau melakukan hal merugikan user lainnya.

POC:
misal ada aplikasi yang memiliki fitur mengubah email di akun mereka, requestnya sebagai berikut:
```
POST /email/change HTTP/1.1
Host: vulnerable-website.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 30
Cookie: session=yvthwsztyeQkAPzeQ5gHgTvlyxHfsAfE

email=wiener@normal-user.com
```
Dari request itu, yang dilakukan aplikasi tersebut hanyalah mengecek cookienya, tetapi tidak ada validasi token csrf. Sehingga attacker membuat sebuah html website berikut : 
```
<html>
    <body>
        <form action="https://vulnerable-website.com/email/change" method="POST">
            <input type="hidden" name="email" value="pwned@evil-user.net" />
        </form>
        <script>
            document.forms[0].submit();
        </script>
    </body>
</html> 
```

Jika korban mengunjungi website ini, maka dia akan mentrigger http request ke website dan browser akan otomatis menginclude session cookienya, sehingga emailnya langsung terganti. [source](https://portswigger.net/web-security/csrf)

5. Yang pertama saya lakukan adalah membuat form terlebih dahulu dan memahami apa yang dilakukan form tersebut, kemudian saya membuat 4 func dari masing" return data json dan xml, kemudian mengatur route untuk tiap endpoint serta membuat tampilan htmlnya.

6. tidak ada

ss-postman : 
1. ![json](assets/json.jpg)
2. ![json_id](assets/json_id.jpg)
3. ![xml](assets/xml.jpg)
4. ![xml_id](assets/xml_id.jpg)