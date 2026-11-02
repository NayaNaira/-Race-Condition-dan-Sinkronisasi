# TI4-Race-Condition-dan-Sinkronisasi

# Analisis Race Condition dan Sinkronisasi Mutex Lock pada Sistem Server Toko UMKM

Repositori ini berisi implementasi simulasi dan analisis *Race Condition* serta solusinya menggunakan primitif sinkronisasi **Mutex Lock** pada lingkungan Linux Ubuntu Server (`srv-toko-250660121067`). Project ini disusun untuk memenuhi Tugas Individu TI-4D mata kuliah Sistem Operasi.

---

## Identitas Server & Penguji
- **Hostname Server:** `srv-toko-250660121067`
- **NIM:** `250660121067`
- **Lingkungan OS:** Linux Ubuntu Server (VM)

---

## Deskripsi Kasus
Simulasi ini menguji keandalan sistem server *e-commerce* Toko UMKM saat menangani skenario *Flash Sale*, di mana **100 thread pembeli** secara simultan berebut stok produk sebanyak **20 unit**.

- **Skenario Unsafe (`flash_sale_unsafe.py`):** Akses variabel terbagi (*shared memory*) tanpa penguncian. Terjadi *context switching* di antara pembacaan dan pengurangan stok, memicu *overselling* (stok akhir bernilai negatif `-2` hingga `-3`).
- **Skenario Safe (`flash_sale_safe.py`):** Proteksi *critical section* menggunakan primitif sinkronisasi **Mutex Lock** (`threading.Lock()`). Menjamin *Mutual Exclusion* sehingga stok akhir konsisten bernilai tepat `0` (transaksi tepat 20 unit, 80 sisa ditolak).

---

## Struktur Berkas Repositori
- `flash_sale_unsafe.py` : Skrip Python simulasi *flash sale* tanpa sinkronisasi (*Race Condition*).
- `flash_sale_safe.py` : Skrip Python simulasi *flash sale* terproteksi *Mutex Lock*.
- `Laporan_TI4D_250660121067.pdf` : Naskah laporan resmi analisis Sistem Operasi lengkap.

---

## Cara Menjalankan Skrip
Jalankan skrip berikut di terminal Linux VM:

```bash
# Masuk ke direktori kerja
cd ~/ti-4d

# Uji skrip tanpa sinkronisasi (Unsafe)
python3 flash_sale_unsafe.py

# Uji skrip terproteksi Mutex Lock (Safe)
python3 flash_sale_safe.py
