1. Cara saya mengimplementasikannya adalah dengan cara mengikuti prosedur yang diberikan dari tutorial0 yaitu mulai dari membuat repository dan menyiapkan dependencies serta membuat project django. Setelah itu saya melakukan registrasi appnya di dalam settings.py. Kemudian membuat models Product sesuai spesifikasi minimal yang diberikan dengan menambahkan beberapa atribut. Kemudian saya melakukan routing agar dapat menjalankan main untuk menampilkan views.py
2. Berdasarkan gambar dibawah dapat dilihat bahwa pertama kali setelah client melakukan request, request akan diteruskan ke urls.py pada level django project dimana akan dilakukan pengecekan endpoint misalnya pada kode ini jika endpoint nya adalah "/admin" maka akan diteruskan ke admin.site.urls, sedangkan sisanya akan langsung diteruskan ke main.urls dikarenakan path yang dicocokkan adalah strings kosong, jika pada case lain request endpoint dari client tidak match dengan urls.py maka aplikasi akan melempar 404 error not found. Jika berhasil ditemukan endpoint yang cocok, maka request selanjutnya akan masuk ke app level URLconf, misal ketika kita melakukan request ke http://IP:Port/ maka selanjutnya akan diteruskan ke main/urls.py, kemudian jika tidak ada endpoint yang match maka aplikasi akan kembali melempar respone 404 error not found, jika ditemukan maka apps akan meneruskan ke views.py dan views.py dapat memanggil models.py jika dibutuhkan untuk mengambil data atau memproses data dari database setelah itu maka akan kembali ke views.py dimana selanjutnya jika aplikasi akan melakukan return response berupa html maka views akan me-render templates terlebih dahulu, sebelum mengembalikan response kepada client. Dalam kode tugas ini adalah menampilkan data nama, npm, dan kelas. <img width="1221" height="245" alt="flow" src="assets/flow.png" />
3. settings.py adalah file konfigurasi utama dari sebuah proyek Django. Semua pengaturan yang mengendalikan jalannya aplikasi Django berada di file ini. settings.py berguna untuk menentukan struktur dasar proyek (BASE_DIR), mengatur mode deployment/production (DEBUG), mengatur akses host/domain (ALLOWED_HOST), mendaftarkan aplikasi (INSTALLED_APPS), konfigurasi database (DATABASES), dll (https://www.geeksforgeeks.org/python/django-settings-file-step-by-step-explanation/)
4. Migrasi database di Django adalah proses yang mengubah perubahan pada model di models.py menjadi perintah SQL yang dijalankan pada database. Ketika developer menambahkan atau mengubah model, Django menggunakan perintah makemigrations untuk membuat file migrasi yang berisi instruksi Python tentang perubahan struktur tabel. Selanjutnya, perintah migrate akan mengeksekusi file migrasi tersebut menjadi query SQL sesuai dengan database yang digunakan, misalnya membuat tabel baru atau menambahkan kolom. Django juga mencatat semua migrasi yang sudah diterapkan dalam tabel khusus django_migrations, sehingga sistem dapat melacak, menghindari duplikasi, dan memungkinkan rollback jika diperlukan.
5. Menurut saya alasan utama adalah karena framework django memakai bahasa python, dimana bahasa python sangat mudah untuk dipelajari dan bukan merupakan bahasa pemrograman yang memiliki syntax yang sulit dimengerti. Selain itu, Django menggunakan pola arsitektur MTV (Model-Template-View) yang membantu pemula memahami alur kerja aplikasi web secara terstruktur, mulai dari request masuk, pemrosesan data, hingga menghasilkan response ke pengguna. Kemudian di matakuliah ini juga kita akan mempelajari framework mobile, django memiliki salah satu keunggulan di sisi ini yaitu dapat langsung digunakan sebagai backend dari aplikasi mobile, sehingga hal ini juga mempermudah.
6. Tidak ada
---
TI3
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