def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                # Lewati baris kosong
                if not baris:
                    continue

                try:
                    # Pisahkan NIM dan nilai
                    nim, teks_nilai = baris.split(",")

                    # Ubah nilai menjadi angka
                    nilai = float(teks_nilai)

                    # Simpan data yang valid
                    data.append((nim.strip(), nilai))

                except ValueError:
                    print(f"Baris {nomor} dilewati: {baris}")

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")

    return data


def tulis_rekap(nama_file, data):
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return

    # Ambil seluruh nilai yang valid
    nilai = [item[1] for item in data]

    # Hitung statistik
    jumlah_data = len(nilai)
    rata_rata = sum(nilai) / jumlah_data
    nilai_minimum = min(nilai)
    nilai_maksimum = max(nilai)
    jumlah_lulus = sum(1 for x in nilai if x >= 60)

    # Tulis hasil rekap ke file
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(f"Jumlah data valid: {jumlah_data}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Minimum: {nilai_minimum:.2f}\n")
        file.write(f"Maksimum: {nilai_maksimum:.2f}\n")
        file.write(f"Jumlah lulus: {jumlah_lulus}\n")

    print(f"Jumlah data valid: {jumlah_data}")
    print(f"Rata-rata: {rata_rata:.2f}")
    print(f"Minimum: {nilai_minimum:.2f}")
    print(f"Maksimum: {nilai_maksimum:.2f}")
    print(f"Jumlah lulus: {jumlah_lulus}")
    print(f"Rekap berhasil disimpan ke {nama_file}")


# Program utama
input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

data = baca_data(input_file)

if data:
    tulis_rekap(output_file, data)