def hitung_biaya_parkir(jenis_kendaraan, durasi):
    if jenis_kendaraan == "mobil":
        tarif = 5000
    elif jenis_kendaraan == "motor":
        tarif = 3000

    total_biaya = tarif * durasi
    return total_biaya

jenis_kendaraan = input("Masukkan jenis kendaraan (mobil/motor): ")
jam_masuk = int(input("Masukkan jam masuk: "))
jam_keluar = int(input("Masukkan jam keluar: "))

durasi_parkir = jam_keluar - jam_masuk

total_biaya = hitung_biaya_parkir(jenis_kendaraan, durasi_parkir)

print("===== TOTAL BIAYA PARKIR =====")
print("Jenis kendaraan:",jenis_kendaraan)
print("Jam masuk      :", jam_masuk)
print("Jam keluar     :", jam_keluar)
print("Durasi pakir   :", durasi_parkir, "jam")
print("Total biaya    : Rp", total_biaya)