class Kamar:
    def __init__(self, nomor_kamar, tipe, harga):
        self.nomor_kamar = nomor_kamar
        self.tipe = tipe
        self.harga = harga
        self.status = "Tersedia"

    def tampilkan_detail(self):
        print(f"Kamar {self.nomor_kamar} | Tipe: {self.tipe} | Harga: {self.harga} | Status: {self.status}")

    def ubah_status(self, status_baru):
        self.status = status_baru


class Pelanggan:
    def __init__(self, nama, no_hp, email):
        self.nama = nama
        self.no_hp = no_hp
        self.email = email

    def pesan_kamar(self, hotel, tanggal_masuk, tanggal_keluar):
        kamar = hotel.cari_kamar_tersedia()
        if kamar:
            return hotel.buat_reservasi(self, kamar, tanggal_masuk, tanggal_keluar)
        else:
            print("Maaf, tidak ada kamar tersedia saat ini.")
            return None


class Reservasi:
    def __init__(self, id_reservasi, pelanggan, kamar, tanggal_masuk, tanggal_keluar):
        self.id_reservasi = id_reservasi
        self.pelanggan = pelanggan
        self.kamar = kamar
        self.tanggal_masuk = tanggal_masuk
        self.tanggal_keluar = tanggal_keluar
        self.status = "Belum Dibayar"

    def konfirmasi(self):
        self.kamar.ubah_status("Dipesan")
        print(f"Reservasi {self.id_reservasi} dikonfirmasi.")

    def batalkan(self):
        self.kamar.ubah_status("Tersedia")
        self.status = "Dibatalkan"
        print(f"Reservasi {self.id_reservasi} telah dibatalkan.")

    def hitung_total(self):
        
        return self.kamar.harga


class Pembayaran:
    def __init__(self, id_pembayaran, reservasi, metode):
        self.id_pembayaran = id_pembayaran
        self.reservasi = reservasi
        self.metode = metode
        self.jumlah = reservasi.hitung_total()
        self.status = "Pending"

    def proses_pembayaran(self):
        self.status = "Lunas"
        self.reservasi.status = "Lunas"
        print(f"Pembayaran {self.id_pembayaran} berhasil. Total: {self.jumlah}")

    def tampil_status(self):
        print(f"Status Pembayaran: {self.status}")


class Hotel:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_kamar = []
        self.daftar_reservasi = []

    def tambah_kamar(self, kamar):
        self.daftar_kamar.append(kamar)

    def cari_kamar_tersedia(self):
        for kamar in self.daftar_kamar:
            if kamar.status == "Tersedia":
                return kamar
        return None

    def buat_reservasi(self, pelanggan, kamar, tanggal_masuk, tanggal_keluar):
        id_res = f"RSV{len(self.daftar_reservasi) + 1:03d}"
        reservasi = Reservasi(id_res, pelanggan, kamar, tanggal_masuk, tanggal_keluar)
        self.daftar_reservasi.append(reservasi)
        reservasi.konfirmasi()
        return reservasi


if __name__ == "__main__":
    hotel = Hotel("Hotel Mawar")
    hotel.tambah_kamar(Kamar(101, "Deluxe", 500000))
    hotel.tambah_kamar(Kamar(102, "Suite", 850000))

    pelanggan1 = Pelanggan("Budi", "08123456789", "budi@gmail.com")

    reservasi1 = pelanggan1.pesan_kamar(hotel, "2025-11-20", "2025-11-21")

    if reservasi1:
        pembayaran1 = Pembayaran("PMB001", reservasi1, "Transfer Bank")
        pembayaran1.proses_pembayaran()
        pembayaran1.tampil_status()
