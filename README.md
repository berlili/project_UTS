Judul : Implementasi Analisis Data Nilai Siswa Menggunakan Python, Docker, dan PostgreSQL

1. Penjelasan aplikasi Python
Aplikasi Python ini dibuat untuk mengolah data nilai siswa secara sederhana. Data nilai diambil dari environment variable, lalu diolah menggunakan pandas untuk menghitung rata-rata, nilai tertinggi, dan nilai terendah.
Hasil pengolahan tersebut kemudian disimpan dalam dua bentuk:
File CSV agar bisa dilihat langsung
Database PostgreSQL supaya bisa digunakan untuk kebutuhan lanjutan

2. Alasan memilih base image
Saya memilih base image Python (misalnya python:3.x-slim) karena sudah menyediakan environment Python yang siap digunakan, sehingga tidak perlu instalasi dari nol. Selain itu, versi slim lebih ringan, jadi proses build dan running container jadi lebih cepat dan efisien.
Base image ini juga cocok dengan kebutuhan aplikasi karena mendukung library seperti pandas, sqlalchemy, dan psycopg2-binary. Dengan begitu, risiko error karena masalah dependency bisa diminimalkan dan aplikasi bisa berjalan lebih stabil.

3. Alur komunikasi antar container (app dan db)
Aplikasi ini menggunakan dua container: satu untuk aplikasi Python dan satu lagi untuk database PostgreSQL.
Komunikasi antara keduanya terjadi melalui jaringan internal Docker Compose. Container aplikasi terhubung ke database menggunakan nama service (db) sebagai host. Jadi, aplikasi tidak perlu tahu alamat IP, cukup menggunakan nama tersebut.
Setelah terhubung, aplikasi akan mengirim data hasil olahan ke database dan menyimpannya sebagai tabel.

4. Langkah menjalankan aplikasi dengan docker-compose
Berikut langkah-langkahnya:
Pastikan sudah install Docker dan Docker Compose
Siapkan semua file dalam satu folder:
app.py
requirements.txt
Dockerfile
docker-compose.yml
Buka terminal di folder tersebut
Jalankan perintah:
docker-compose up --build
Tunggu proses selesai, nanti:
Aplikasi akan otomatis berjalan
Data akan diproses
Hasil tersimpan ke file CSV dan database
