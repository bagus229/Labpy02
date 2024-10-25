harga_reguler = 50000
harga_vip = 100000

tipe_tiket = input("Pilih tipe tiket (Reguler/VIP): ").strip().lower()
status_member = input("Apakah Anda memiliki kartu member? (Ya/Tidak): ").strip().lower()

if tipe_tiket == 'reguler':
    harga = harga_reguler
elif tipe_tiket == 'vip':
    harga = harga_vip
else:
    print("Tipe tiket tidak valid.")
    exit()

diskon = 0
total_harga = harga

diskon = total_harga * 0.2 if status_member == 'ya' else 0
total_harga -= diskon

print(f"Total harga yang harus dibayar: Rp{total_harga:.2f}")