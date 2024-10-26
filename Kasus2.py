
# Program Kalkulator Sederhana

# Input dari pengguna
angka1 = float(input("Masukkan angka pertama: "))
angka2 = float(input("Masukkan angka kedua: "))
operator = input("Pilih operator (+, -, *, /): ")

# Menghitung hasil sesuai dengan operator yang dipilih
if operator == '+':
    hasil = angka1 + angka2
    operasi = "penjumlahan"
elif operator == '-':
    hasil = angka1 - angka2
    operasi = "pengurangan"
elif operator == '*':
    hasil = angka1 * angka2
    operasi = "perkalian"
elif operator == '/':
    # Cek jika pembagi adalah nol
    if angka2 == 0:
        hasil = "Error: Pembagian dengan nol tidak diizinkan."
    else:
        hasil = angka1 / angka2
        operasi = "pembagian"
else:
    hasil = "Error: Operator tidak valid."

# Menampilkan hasil
if isinstance(hasil, str):
    print(hasil)  # Menampilkan pesan error
else:
    print(f"Hasil {operasi} antara {angka1} dan {angka2} adalah: {hasil}")
