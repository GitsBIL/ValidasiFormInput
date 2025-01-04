# Validasi Input
Nama    :   Nabil Putra Alamsyah
Kelas   :   312410376

Program Python ini digunakan untuk memvalidasi data input pada sistem pendaftaran online. Program memastikan bahwa data yang dimasukkan oleh pengguna sesuai dengan ketentuan berikut:
    - Nama Lengkap: Hanya boleh mengandung huruf dan spasi.
    - Nomor Telepon: Hanya boleh berisi angka.
    - Email: Harus mengandung karakter @ dan . .
Jika semua data valid, program akan menampilkan pesan konfirmasi pendaftaran. Namun, jika terdapat kesalahan, program akan memberikan pesan error yang spesifik untuk setiap input yang tidak valid.

# Penjelasan

## 1. Mengimpor Library

![Gambar](./Gambar/gambar%201.png)

    - Library re digunakan untuk operasi regular expression (regex).
    - Regex sangat berguna untuk memvalidasi pola teks, seperti memastikan bahwa nama hanya mengandung huruf dan spasi.

## 2. Fungsi Validasi Nama

![Gambar](./Gambar/gambar%202.png)

    - Fungsi ini menerima parameter name (nama lengkap yang diinput oleh pengguna).
    - Menggunakan re.fullmatch(r"[A-Za-z ]+", name) untuk memeriksa apakah name hanya mengandung huruf (A-Z, a-z) dan spasi.
Regex:
    - A-Za-z: Karakter huruf besar dan kecil.
    - : Karakter spasi.
    - +: Satu atau lebih karakter dari pola sebelumnya.
    - Contoh valid: "Bang Alam".
    - Contoh tidak valid: "Bang123" (ada angka).
    - Jika validasi gagal, fungsi mengembalikan pesan error.
    - Jika validasi berhasil, fungsi mengembalikan None.

## 3. Fungsi Validasi Nomor Telepon

    ![Gambar]()

    - Fungsi ini menerima parameter phone (nomor telepon yang diinput pengguna).
    - Menggunakan .isdigit() untuk memeriksa apakah semua karakter dalam phone adalah angka.
    - Contoh valid: "081234567890".
    - Contoh tidak valid: "0812abcd" (mengandung huruf).
    - Jika validasi gagal, fungsi mengembalikan pesan error.
    - Jika validasi berhasil, fungsi mengembalikan None.

## 4. Fungsi Validasi Email

    ![Gambar]()

    - Fungsi ini menerima parameter email (email yang diinput pengguna).
    - Memastikan email mengandung karakter @ dan ..
Menggunakan kondisi sederhana:
    - if "@" not in email: Memeriksa apakah email tidak mengandung @.
    - or "." not in email: Memeriksa apakah email tidak mengandung ..
    - Contoh valid: "bangalam@example.com".
    - Contoh tidak valid: "bangalamexample" (tidak ada @ atau .).
    - Jika validasi gagal, fungsi mengembalikan pesan error.
    - Jika validasi berhasil, fungsi mengembalikan None.

## 5. Program Utama

    ![Gambar]()

### Penjelasan:
    
    1. Menampilkan pesan awal:

        [Gambar]()

        -  Memberikan instruksi kepada pengguna untuk memasukkan data.

    2. Menerima input pengguna:

        [Gambar]()

        - Fungsi input() digunakan untuk mengambil data dari pengguna.
        - .strip() menghapus spasi di awal dan akhir input.
    
    3. Membuat daftar untuk pesan error:

        [Gambar]()

        - Daftar ini digunakan untuk menyimpan pesan error yang muncul selama validasi.

    4. Memanggil fungsi validasi:

        [Gambar]()

        - Memeriksa setiap input menggunakan fungsi validasi.
        - Jika fungsi validasi mengembalikan pesan error, tambahkan ke daftar errors.

    5. Menampilkan hasil validasi:

        [Gambar]()

        - Jika daftar errors tidak kosong, artinya ada kesalahan.
        - Tampilkan semua pesan error.
        - Jika errors kosong, artinya semua validasi berhasil, dan tampilkan pesan sukses.

    6. Menjalankan Program

        [Gambar]()

        - Kondisi ini memastikan bahwa program utama hanya akan dijalankan jika file Python ini dijalankan secara langsung.
        - Jika file ini diimpor ke program lain, fungsi main() tidak akan otomatis dijalankan.

## Output Program:

### Input Valid :

    [Gambar]()

### Input Tidak Valid :

    [Gambar()]




      