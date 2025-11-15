class Meja:
    def __init__(self, nomor_meja, kapasitas):
        self.nomor_meja = nomor_meja
        self.kapasitas = kapasitas
        self.status = "Tersedia"

    def cekStatus(self):
        return self.status

    def ubahStatus(self, status_baru):
        self.status = status_baru


class Reservasi:
    def __init__(self, id_reservasi, waktu, pelanggan, meja):
        self.id_reservasi = id_reservasi
        self.waktu = waktu
        self.pelanggan = pelanggan
        self.meja = meja

    def konfirmasi(self):
        self.meja.ubahStatus("Terpesan")
        print(f"Reservasi {self.id_reservasi} dikonfirmasi untuk meja {self.meja.nomor_meja}")

    def batalkan(self):
        self.meja.ubahStatus("Tersedia")
        print(f"Reservasi {self.id_reservasi} dibatalkan.")


class Pelanggan:
    def __init__(self, nama, nomor_hp):
        self.nama = nama
        self.nomor_hp = nomor_hp

    def pesanMeja(self, restoran, waktu):
        meja = restoran.cariMejaTersedia()
        if meja:
            reservasi = Reservasi("R001", waktu, self, meja)
            reservasi.konfirmasi()
            return reservasi
        else:
            print("Tidak ada meja tersedia.")


class Restoran:
    def __init__(self, nama_restoran, daftar_meja):
        self.nama_restoran = nama_restoran
        self.daftar_meja = daftar_meja

    def cariMejaTersedia(self):
        for meja in self.daftar_meja:
            if meja.cekStatus() == "Tersedia":
                return meja
        return None



meja1 = Meja(1, 4)
meja2 = Meja(2, 2)
restoran = Restoran("Rasa Nusantara", [meja1, meja2])
pelanggan1 = Pelanggan("Budi", "08123456789")

reservasi1 = pelanggan1.pesanMeja(restoran, "19:00")
reservasi1.batalkan()
