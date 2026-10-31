# Pertemuan 12 - File I/O dan Error Handling

## Identitas Mahasiswa
- **Nama:** Sekar Wahyuningrum
- **NIM:** 2225250095
- **Mata Kuliah:** Algoritma dan Pemrograman
- 

## 1. Tujuan Praktikum

Praktikum ini bertujuan untuk mempelajari cara membaca dan menulis file menggunakan Python, memproses data teks, serta menangani error menggunakan `try-except`.

Praktikum juga melatih penggunaan file input dan output untuk mengolah data nilai mahasiswa.

## 2. Materi yang Dipelajari

- Membaca file menggunakan mode `r`.
- Menulis file menggunakan mode `w`.
- Menambahkan teks menggunakan mode `a`.
- Menggunakan `with open()` dan `encoding="utf-8"`.
- Memproses data menggunakan `strip()` dan `split()`.
- Mengonversi data menggunakan `float()`.
- Menangani `FileNotFoundError` dan `ValueError`.
- Menghitung statistik nilai dari file.
- Menyimpan hasil pengolahan ke file output.

## 3. Struktur Repository

```text
pertemuan-12-file-io-2225250095/
├── README.md
├── .gitignore
├── data/
│   ├── catatan.txt
│   ├── nilai.txt
│   └── hasil_rekap.txt
├── latihan/
│   ├── 01_tulis_file.py
│   ├── 02_baca_file.py
│   ├── 03_append_file.py
│   ├── 04_proses_baris.py
│   ├── 05_file_not_found.py
│   └── 06_value_error.py
└── tugas/
    └── rekap_nilai_file.py
```

## 4. Fungsi Setiap Folder

- **data/**: Menyimpan file teks untuk input dan output program.
- **latihan/**: Menyimpan enam program latihan file I/O dan penanganan error.
- **tugas/**: Menyimpan program utama untuk merekap nilai mahasiswa.
- **README.md**: Mendokumentasikan identitas, tujuan, cara menjalankan program, dan hasil pengujian.
- **.gitignore**: Mengabaikan file tertentu agar tidak diunggah ke GitHub.

## 5. Format File Input

File `data/nilai.txt` menggunakan format:

```text
NIM,nilai
```

Contoh data:

```text
A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88
```

Data `A004,abc` digunakan untuk menguji penanganan nilai yang tidak valid.

## 6. Cara Menjalankan Program

Jalankan perintah berikut dari terminal di folder utama proyek.

Menjalankan latihan:

```bash
python latihan/01_tulis_file.py
python latihan/02_baca_file.py
python latihan/03_append_file.py
python latihan/04_proses_baris.py
python latihan/05_file_not_found.py
python latihan/06_value_error.py
```

Menjalankan tugas utama:

```bash
python tugas/rekap_nilai_file.py
```

Jika diperlukan, gunakan `python3` sebagai pengganti `python`.

## 7. Hasil Pengujian Tugas Utama

| No. | Pengujian | Hasil yang Diharapkan |
|---|---|---|
| 1 | Semua data valid | Data diproses dan statistik dihitung. |
| 2 | File tidak ditemukan | Pesan kesalahan ditampilkan tanpa menghentikan program secara kasar. |
| 3 | Nilai tidak valid | Baris yang salah dilewati dan data lainnya tetap diproses. |
| 4 | Baris kosong | Baris kosong dilewati. |
| 5 | Nilai batas 60 | Nilai 60 dihitung sebagai lulus. |
| 6 | Penyimpanan rekap | Hasil rekap disimpan ke `data/hasil_rekap.txt`. |

### Hasil Perhitungan Data Contoh

- Jumlah data valid: 5
- Rata-rata: 83.40
- Nilai minimum: 74.00
- Nilai maksimum: 92.00
- Jumlah lulus: 5

**Catatan:** Hasil tersebut merupakan hasil yang diharapkan dari data contoh. Pastikan program dijalankan untuk memverifikasi hasil aktual.

## 8. Error yang Ditangani

**FileNotFoundError** terjadi ketika program mencoba membuka file yang tidak tersedia.

**ValueError** terjadi ketika data tidak dapat dikonversi menjadi angka atau format baris tidak sesuai.

Kedua error ditangani menggunakan `try-except` agar program dapat memberikan pesan yang jelas dan tetap memproses data valid.

## 9. Kesimpulan

Melalui praktikum Pertemuan 12, saya mempelajari cara menyimpan, membaca, dan mengolah data menggunakan file dalam Python. Saya juga memahami perbedaan mode `r`, `w`, dan `a`, serta penggunaan `try-except` untuk menangani kesalahan.

Pada tugas utama, data nilai dibaca dari file, divalidasi, dihitung statistiknya, dan disimpan ke file hasil rekap. Praktikum ini membantu saya memahami pentingnya validasi data dan penanganan error dalam membuat program yang lebih aman.

## 10. Refleksi

Saya memahami bahwa file memungkinkan data tetap tersimpan meskipun program telah selesai dijalankan. Saya juga belajar bahwa data yang tidak valid tidak harus menghentikan seluruh proses jika kesalahan ditangani dengan tepat.

Kesalahan yang perlu diperhatikan adalah nama dan lokasi file, pemilihan mode pembukaan file, serta format data yang dibaca. Pengujian membantu memastikan program menghasilkan keluaran sesuai kebutuhan.

## 11. Sumber Referensi

1. Bahan Ajar Algoritma dan Pemrograman Pertemuan 12: File Input-Output dan Penanganan Error Dasar.
2. Downey, A. B. (2015). *Think Python: How to Think Like a Computer Scientist* (2nd ed.). Green Tea Press.


---

