# Tugas Praktikum 1: Unit Testing dengan Python & unittest

Proyek ini adalah implementasi sederhana dari sistem manajemen buku (`BookManager`) menggunakan **Python**. Tujuan utamanya adalah untuk mempraktikkan konsep **Unit Testing** dengan menggunakan library standar Python, yaitu `unittest`.

Proyek ini dibuat sebagai bagian dari **Tugas Praktikum Pengujian Perangkat Lunak (PPL)**.

---

### ## 🚀 Teknologi yang Digunakan
* **Python 3**: Bahasa pemrograman utama.
* **unittest**: Framework unit testing bawaan Python.
* **Visual Studio Code**: Sebagai editor kode utama.

---

### ## ✨ Fitur Utama
* `book.py`: Class entitas yang merepresentasikan sebuah buku dengan atribut judul, penulis, dan tahun.
* `book_manager.py`: Class service untuk mengelola koleksi buku, dengan fungsi:
    * Menambah buku baru.
    * Menghapus buku berdasarkan judul.
    * Mendapatkan semua daftar buku.
    * Mencari buku berdasarkan penulis.
    * Mencari buku berdasarkan tahun terbit.

---

### ## ⚙️ Cara Menjalankan Tes
1.  Pastikan Anda memiliki **Python 3** terinstal di komputer Anda.
2.  Clone repository ini.
3.  Buka terminal atau Command Prompt di dalam folder root proyek ini.
4.  Jalankan perintah berikut untuk memulai semua unit test:
    ```bash
    python -m unittest test_bookmanager.py -v
    ```
5.  Anda juga bisa menjalankan tes melalui **Test Explorer** di Visual Studio Code.

---

### ## 👨‍💻 Dibuat oleh
* **Nama**: [Rifqi Firmansyah]
* **NIM**: [230109029]
