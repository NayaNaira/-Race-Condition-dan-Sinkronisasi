import threading
import time

# Shared Memory (Variabel Terbagi di memori utama)
stok_produk = 20        # Stok produk flash sale P999
berhasil_checkout = 0
gagal_stok_habis = 0

def proses_checkout(id_pembeli):
    global stok_produk, berhasil_checkout, gagal_stok_habis

    # --- CRITICAL SECTION (TANPA PROTEKSI / UNSAFE) ---
    if stok_produk > 0:
        time.sleep(0.001)  # Simulasi jeda pencatatan / I/O
        stok_produk -= 1
        berhasil_checkout += 1
    else:
        gagal_stok_habis += 1
    # --------------------------------------------------

if __name__ == "__main__":
    print("=== SIMULASI FLASH SALE (UNSAFE - TANPA MUTEX) ===")
    threads = []

    # 100 Pembeli (Thread) merebut 20 Stok bersamaan
    for i in range(100):
        t = threading.Thread(target=proses_checkout, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Stok Akhir        : {stok_produk}")
    print(f"Berhasil Checkout : {berhasil_checkout}")
    print(f"Gagal (Stok Habis): {gagal_stok_habis}")
    if stok_produk < 0 or berhasil_checkout > 20:
        print("HASIL: TERJADI OVERSELLING / RACE CONDITION!")
